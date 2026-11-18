"""Independent, CPU-only checks of five engineering artifacts. No hardware/TCAD execution."""
from pathlib import Path
import json, sys, hashlib, platform, tempfile
import numpy as np
import scipy
from scipy.linalg import solve_continuous_are
from scipy.signal import cont2discrete, place_poles
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
SRC=(ROOT/'sources') if (ROOT/'sources').is_dir() else ROOT.parent/'sources'
(ROOT/'figures').mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':160,'savefig.dpi':220})
results={'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},'scope':'Independent numerical reanalysis; historical plots are not new measurements.'}

def rst(length=.35,beta=.5,gamma=30):
    a2=9.81/length;a=np.sqrt(a2)
    D=np.poly([-a,-a,-beta,-gamma,-beta-1j,-beta+1j]).real
    c1,c2,c3,c4,c5,c6=D[1:]
    R=np.array([(1-a2-c2)/a2,(c1*(1-a2)-c3)/a2,-(a2+c4)/a2,-(a2*c1+c5)/a2,-c6/a2])
    S=np.convolve([1,0,1,0],[1,c1]);t2=R[-1]/(beta*gamma)
    M=np.array([[1-beta*gamma,-(beta+gamma)],[-(beta+gamma),beta*gamma-1]])
    t0,t1=np.linalg.solve(M,[R[0]-R[2]+R[4]-(beta*gamma-1)*t2,R[3]-R[1]-(beta+gamma)*t2])
    T=np.convolve([1,beta+gamma,beta*gamma],[t0,t1,t2])
    actual=np.polyadd(np.convolve([1,0,-a2],S),-a2*R)
    residual=float(np.max(np.abs(actual-D))/np.max(np.abs(D)))
    assert residual<1e-12
    for s in [0,1j]: assert abs((-a2*np.polyval(T,s)/np.polyval(actual,s))-1)<1e-10
    return R,S,T,D,residual

R,S,T,D,res=rst();lengths=np.linspace(.16,.60,221);fixed=[];redesigned=[]
for L in lengths:
    char=np.polyadd(np.convolve([1,0,-9.81/L],S),(-9.81/L)*R)
    fixed.append(float(np.max(np.roots(char).real)))
    redesigned.append(float(np.max(np.roots(rst(L)[3]).real)))
sample=[]
for L in [.16,.23,.28,.35,.60]:
    roots=np.roots(np.polyadd(np.convolve([1,0,-9.81/L],S),(-9.81/L)*R))
    sample.append({'length_m':L,'max_real_pole_fixed':float(max(roots.real))})
fig,ax=plt.subplots(figsize=(6.7,3.25));ax.plot(lengths,fixed,label='Fixed controller, design L=0.35 m',color='#244a68');ax.plot(lengths,redesigned,'--',label='Controller resynthesized at each L',color='#a04f45');ax.axhline(0,color='black',lw=.8);ax.set(xlabel='Pendulum length L (m)',ylabel='Largest pole real part (1/s)',ylim=(-.505,-.485));ax.legend(fontsize=8);fig.tight_layout();fig.savefig(ROOT/'figures/rst.png');plt.close(fig)
results['rst']={'R':R.tolist(),'S':S.tolist(),'T':T.tolist(),'D':D.tolist(),'bezout_relative_residual':res,'samples':sample,'grid_cases':len(lengths),'fixed_grid_max_real':max(fixed),'source_sign_issue':'Report p.13 prints r2 positive for the initial design, while coefficient matching and source yield negative.', 'initial_r2':float(rst(beta=1,gamma=10)[0][2])}
np.savetxt(ROOT/'rst-length-sweep.csv',np.c_[lengths,fixed,redesigned],delimiter=',',header='length_m,max_real_fixed,max_real_redesigned',comments='')

# Twin rotor: exact source parameters and a deliberate transcription comparison.
Ke=.29;Kt=1.336;Kl=-5.21894;w=.7;xi=.08;tau=10
A=np.array([[-2*xi*w,-w*w,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,Kl/tau,-1/tau]],float)
B=np.array([[Ke*w*w,Ke*w*w],[0,0],[Kt,-Kt],[0,0],[0,0]],float);C=np.array([[0,1,0,0,0],[0,0,0,0,1]],float)
Aa=np.block([[A,np.zeros((5,2))],[C,np.zeros((2,2))]]);Ba=np.vstack([B,np.zeros((2,2))]);Q=np.diag([0]*5+[40,40]);Ash=Aa+.5*np.eye(7)
P=solve_continuous_are(Ash,Ba,Q,np.eye(2));K=Ba.T@P;E=np.linalg.eigvals(Aa-Ba@K);Eshift=np.linalg.eigvals(Ash-Ba@K)
resid=np.linalg.norm(P@Ash+Ash.T@P-P@Ba@Ba.T@P+Q)/max(1,np.linalg.norm(Q))
assert resid<1e-8 and max(E.real)<-.5
Ac=np.array([[0,1],[-.8038**2,-2*.0912*.8038]]);Cv=np.array([[1.,0.]])
variants=[]
for label,b in [('as coded',.3299*.8038),('from stated transfer function',.3299*.8038**2)]:
    F,G,_,_,_=cont2discrete((Ac,np.array([[0.],[b]]),Cv,np.zeros((1,1))),.05)
    Fe=np.block([[F,np.zeros((2,1))],[Cv,np.ones((1,1))]]);Ge=np.vstack([G,[[0.]]]);cp=np.linalg.eigvals(np.block([[Ac,np.zeros((2,1))],[Cv,np.zeros((1,1))]]));target=np.exp((-1+1j*cp.imag)*.05)
    gain=place_poles(Fe,Ge,target).gain_matrix
    variants.append({'model':label,'input_coefficient':b,'dc_gain':b/.8038**2,'G':G.ravel().tolist(),'gain_Tc1':gain.ravel().tolist()})
fig,ax=plt.subplots(figsize=(6.7,3.25));ax.scatter(Eshift.real,Eshift.imag,marker='x',s=65,label='Eigenvalues returned for shifted design');ax.scatter(E.real,E.imag,facecolors='none',edgecolors='#244a68',s=65,label='Physical augmented closed-loop poles');ax.axvline(-.5,color='#a04f45',ls='--',lw=1);ax.set(xlabel='Real part (1/s)',ylabel='Imaginary part (rad/s)');ax.legend(fontsize=8);fig.tight_layout();fig.savefig(ROOT/'figures/twin.png');plt.close(fig)
results['twin']={'K':K.tolist(),'physical_eigenvalues':[[float(x.real),float(x.imag)] for x in E],'shifted_eigenvalues':[[float(x.real),float(x.imag)] for x in Eshift],'care_relative_residual':float(resid),'controllability_rank':int(np.linalg.matrix_rank(np.hstack([np.linalg.matrix_power(Aa,k)@Ba for k in range(7)]))),'siso_variants':variants,'reported_parameter_conflicts':{'damping_text':.05,'damping_code':.08,'yaw_tau_text':20,'yaw_tau_code':10}}

# CMM rank and robustness: declared synthetic experiment, never a machine calibration.
n=240;i=np.arange(n);theta=i*np.pi*(3-np.sqrt(5));rng=np.random.default_rng(20261118)
def normals(z):
    return np.c_[np.sqrt(1-z*z)*np.cos(theta),np.sqrt(1-z*z)*np.sin(theta),z]
designs={'planar':normals(np.zeros(n)),'thin_band_1deg':normals(np.linspace(-np.sin(np.pi/180),np.sin(np.pi/180),n)),'band_45deg':normals(np.linspace(-np.sqrt(.5),np.sqrt(.5),n)),'sphere':normals(np.linspace(-1+1/n,1-1/n,n))}
geometry=[]
for name,N in designs.items():
    X=np.c_[N,np.ones(n)];sv=np.linalg.svd(X,compute_uv=False);rank=np.linalg.matrix_rank(X)
    geometry.append({'geometry':name,'rank':int(rank),'singular_values':sv.tolist(),'condition':float(sv[0]/sv[-1]) if rank==4 else None})
def huber(X,y):
    b=np.linalg.lstsq(X,y,rcond=None)[0]
    for _ in range(100):
        r=y-X@b;s=max(1.4826*np.median(abs(r-np.median(r))),1e-12);wt=np.minimum(1,1.345*s/np.maximum(abs(r),1e-15));new=np.linalg.lstsq(X*np.sqrt(wt[:,None]),y*np.sqrt(wt),rcond=None)[0]
        if np.linalg.norm(new-b)<1e-10: return new
        b=new
    return b
X=np.c_[designs['band_45deg'],np.ones(n)];truth=np.array([1.,-2.,.5,.8]);errors=[]
for run in range(100):
    y=X@truth+rng.normal(0,.15,n);spikes=rng.choice(n,12,replace=False);y[spikes]+=3.
    ols=np.linalg.lstsq(X,y,rcond=None)[0];rob=huber(X,y);errors.append([np.linalg.norm(ols-truth),np.linalg.norm(rob-truth)])
errors=np.array(errors);assert geometry[0]['rank']==3 and geometry[2]['rank']==4
fig,(a,b)=plt.subplots(1,2,figsize=(6.7,3.25));a.bar(['Plane','1 deg','45 deg','Sphere'],[x['singular_values'][-1] for x in geometry],color='#244a68');a.set(ylabel='Smallest singular value');b.boxplot(errors,tick_labels=['Least squares','Huber IRLS'],showfliers=False);b.set(ylabel='Parameter-vector error (micrometres)');fig.tight_layout();fig.savefig(ROOT/'figures/cmm.png');plt.close(fig)
results['cmm']={'geometries':geometry,'synthetic':{'seed':20261118,'points':n,'replicates':100,'truth_um':truth.tolist(),'noise_std_um':.15,'positive_outlier_count':12,'outlier_increment_um':3.,'median_error_ols_um':float(np.median(errors[:,0])),'median_error_huber_um':float(np.median(errors[:,1])),'meaning':'Synthetic conditional test, no physical CMM uncertainty or calibration claim.'}}
np.savetxt(ROOT/'cmm-monte-carlo.csv',errors,delimiter=',',header='ols_parameter_error_um,huber_parameter_error_um',comments='')

# Hydraulic arithmetic, with one explicitly stated density and gravity convention.
rho=1000.;g=9.81;N=1500.;Qv=.132;H=3.8;Pwater=rho*g*Qv*H
cfdeff=1760/(rho*g*.144*3.6);windavail=.5*1.2*np.pi*.075**2*10**3;windpower=.239*windavail
Hs=np.linspace(2,5,101);fig,ax=plt.subplots(figsize=(6.7,3.25));ax.plot(Hs,rho*g*.132*Hs/1000,label='Hydraulic input, Q=0.132 m3/s');ax.plot(Hs,.92*rho*g*.132*Hs/1000,label='Shaft output at assumed efficiency 0.92');ax.axhline(5,color='#a04f45',ls='--',label='5 kW target');ax.axvline(3.8,color='grey',ls=':');ax.set(xlabel='Net head (m)',ylabel='Power (kW)');ax.legend(fontsize=8);fig.tight_layout();fig.savefig(ROOT/'figures/turbine.png');plt.close(fig)
results['turbine']={'hydraulic_input_W':Pwater,'shaft_at_eta_092_W':.92*Pwater,'eta_required_5kW':5000/Pwater,'head_required_5kW_eta092_m':5000/(.92*rho*g*.132),'cfd_implied_efficiency':cfdeff,'cfd_torque_Nm':1760/(N*np.pi/30),'two_reported_runners_W':3520,'wind_available_W':windavail,'wind_power_from_Cp_W':windpower,'wind_torque_Nm':windpower/190.5,'wind_tip_speed_ratio':.075*190.5/10,'scope':'Arithmetic consistency only, no CFD or experimental rerun.'}

sys.path.insert(0,str(SRC/'HeMT-GaN-Transistor'))
from tools.ecorce_deck import parse_device,parse_stimulus,validate_pair
folder=SRC/'HeMT-GaN-Transistor/models/ecorce/lateral-gan-hemt';dev=folder/'device.dev';sti=folder/'transfer_gate_0_to_5V.sti';device=parse_device(dev);stim=parse_stimulus(sti)
assert validate_pair(dev,sti)==[]
with tempfile.TemporaryDirectory() as tmp:
    negative=Path(tmp)/'bad.sti';txt=sti.read_text();contact=stim['biases'][0]['contact'];negative.write_text(txt.replace(contact,'NONEXISTENT_CONTACT'));detected=validate_pair(dev,negative);assert any('unknown contact' in e.lower() for e in detected)
results['gan']={'device':device,'stimulus':stim,'validation_errors':validate_pair(dev,sti),'negative_test_errors':detected,'hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [dev,sti]},'scope':'Static inspection of the recovered lateral HEMT only. No execution of Ecorce or verification of a vertical architecture.'}
fig,ax=plt.subplots(figsize=(6.7,3.25));labels=list(device['enabled_physics']);values=[int(v) for v in device['enabled_physics'].values()];ax.barh(labels,values,color='#244a68');ax.set(xticks=[0,1],xticklabels=['disabled','enabled'],xlabel='Explicit switches in the recovered deck');fig.tight_layout();fig.savefig(ROOT/'figures/gan.png');plt.close(fig)

# Immutable input manifest for all reports and source code actually used.
inputs=[]
for repo in ['RST-controller-for-an-inverted-pendulum','Control-of-an-instable-system-using-digital-state-feedback','-Spatial-Verification-of-a-Coordinate-Measuring-Machine','-Design-of-a-Turbomachine','HeMT-GaN-Transistor']:
    for p in (SRC/repo).rglob('*'):
        if p.is_file() and (p.suffix.lower()=='.pdf' or p.name in ['rst_pendulum_synthesis.m','integral_state_feedback_pole_placement.m','lqr_integral_control.m','Metrology_Correction.m','affinity_law_scaling.m','ecorce_deck.py']):inputs.append({'path':str(p.relative_to(SRC)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
results['input_manifest']=inputs
for section in ('device','stimulus'):
    results['gan'][section]['path']=str(Path(results['gan'][section]['path']).relative_to(SRC))
(ROOT/'results.json').write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({key:({k:v for k,v in value.items() if k not in ['device','stimulus','input_manifest']} if isinstance(value,dict) else value) for key,value in results.items() if key not in ['input_manifest']},indent=2))

# LncRNA_Target:A target prediction tool for long non coding RNA and messenger RNA<br />
Long noncoding RNAs (lncRNAs) are noncoding transcripts having length longer than 200 nucleotides. These molecules play a key role in various biological processes by regulating gene expression. Recently it has been demonstrated that lncRNAs can bind to proteins, DNA and even mRNAs. Such diversity in their binding capability necessitates understanding the binding mechanisms and rules exhibited by them.<br />
Till date several research groups have come up with many target prediction tools. However, the detailed mechanism of an lncRNA interacting with mRNA still remains to be understood. Multiple binding sites between the two RNAs (i.e. lncRNAs and mRNAs) remains to be the most critical factor decisive of an efficient interaction. Besides, tools predicting these interactions using machine learning algorithms do not predict the interaction score efficiently due to unavailability of enough negative datasets.<br />
LncrTar, is a target prediction tool, which overcomes the above mentioned hurdles and identifies the probable binding sites between lncRNA and mRNA along with determination of interaction energy. LncrTar comes up with two major findings. These calculations are done on the basis of the experimentally validated positive lncRNA-mRNA interaction information reported by . The feature set has been prepared from the sequence and binding information. Interaction confidence of the input sequence pair has been evaluated by 7 different machine learning models. The interaction confidence for input pair helps user to select the most putative interaction. The accessible segments between lncRNA and mRNA has been identified by using AccessE algorithm designed by us. The binding information among the accessible segments of lncRNA and its target can be visualized as well as downloaded.
### Prequisites
Ubuntu environment<br />
Install unrar if not there ( >sudo apt install unrar)<br />
Anaconda for Python 3.7<br />
LightGBM <br />
RNAstructure version 6.0 (64-bit), released on September 21, 2017.<br />


### How to Install and Run
1.  create an account and add to sudoers<br /> 
    >$>sudo adduser lncpred<br />
2.  Login as root user <br />
    >$>sudo su <br />
3.  Attach user account to sudoers file <br />
    >$>usermod -aG sudo lncpred<br />
4.  Download and Install PARASOR
    >$>cd /home/lncpred<br />
    >$> git clone https://github.com/carushi/ParasoR <br />
    >$>cd ParasoR<br />
    >$>./configure<br />
    >$>make<br />
    >$>make install<br />
    >$>autoreconf -ivf<br />
5.  Download LncRTPred project files from github
    >$> git clone https://github.com/parida007/LncRTPred <br />
6. Download and Install RNAstructure 6.0 sep 21 2017;Command line interfaces;download 64bit-linux(53.71mb)<br />
    >$>cd /home/lncpred/ParasoR/script<br />
    >$>wget http://rna.urmc.rochester.edu/Releases/6.0/RNAstructureLinuxTextInterfaces64bit.tgz <br />
    >$>tar -xvzf RNAstructureLinuxTextInterfaces64bit.tgz <br />
    >$>cd RNAstructure <br />
    >$>cp cal_hybrid.py . (Copy cal_hybrid.py inside RNAstructure)<br />
7.  Keep all the python (.py) and machine learning moel (.sav) files in /home/lncpred/ParasoR/script/ <br />
    >$>Main.py<br />
    >$>Extract_Feature.py<br />
    >$>cal_modified_hybrid_energy1.py<br />
    >$>cal_stem.py<br />
    >$>count_base_v1.py<br />
    >$>features_predict.py<br />
    >$>basecount.py<br />
    >$>Dataset_Generator.py<br />
    >$>ML_Prediction.py<br />
    >$>Predict_Binding.py<br />
    >$>baggingPU.py<br />
    >$>Model_Files.rar[extract the model files from the rar files and unrar using <b>unrar x Model_Files.rar</b>]<br /> 
    >$>max_base_span.txt<br />
    **EVERY call must be in root Mode
8.  Install Anaconda3 (All the steps in section 7 and section 8 must be executed in non root mode)
    >$>wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh <br />
    *must be installed in non-root mode<br />
    >$>sh *.sh <br />
    set PATH variable <br />
    PATH="/home/lncpred/anaconda3/bin:$PATH"<br />
       
9.  Install LightGBM, Biopython
    >$>pip install lightgbm <br />
    >$>pip install biopython <br />
10.  Copy all the html and php files and supporting folders to 
    /home/user/ParasoR/script/<br />
    >$>cp /home/lncpred/ParasoR/script/index_1.html .<br />
    >$>cp /home/lncpred/ParasoR/script/*.php .<br />
    >$>cp -a /home/lncpred/ParasoR/script/contactform/. contactform/<br />
    >$>cp -a /home/lncpred/ParasoR/script/img/. img/<br />
    >$>cp -a /home/lncpred/ParasoR/script/lib/. lib/<br />
    >$>cp -a /home/lncpred/ParasoR/script/css/. css/<br />
    >$>cp -a /home/lncpred/ParasoR/script/js/. js/<br />
11.  To run lncpred:<br />
    >$>python Main.py<br />
    **All the input must be named as query.fa (LncRNA sequences) & target.fa(mRNA sequences)<br />
    Result:<br />
    a)final_energy_data.txt<br />
    b)LncRNA_MRNA_Binding_Prediction.csv
    
    
    

 

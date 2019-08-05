# LncRTar:A target prediction tool for long non coding RNA and messenger RNA.<br />
Long noncoding RNAs (lncRNAs) are noncoding transcripts having length longer than 200 nucleotides. These molecules play a key role in various biological processes by regulating gene expression. Recently it has been demonstrated that lncRNAs can bind to proteins, DNA and even mRNAs. Such diversity in their binding capability necessitates understanding the binding mechanisms and rules exhibited by them.<br />
Till date several research groups have come up with many target prediction tools. However, the detailed mechanism of an lncRNA interacting with mRNA still remains to be understood. Multiple binding sites between the two RNAs (i.e. lncRNAs and mRNAs) remains to be the most critical factor decisive of an efficient interaction. Besides, tools predicting these interactions using machine learning algorithms do not predict the interaction score efficiently due to unavailability of enough negative datasets.<br />
LncrTar, is a target prediction tool, which overcomes the above mentioned hurdles and identifies the probable binding sites between lncRNA and mRNA along with determination of interaction energy. LncrTar comes up with two major findings. These calculations are done on the basis of the experimentally validated positive lncRNA-mRNA interaction information reported by . The feature set has been prepared from the sequence and binding information. Interaction confidence of the input sequence pair has been evaluated by 7 different machine learning models. The interaction confidence for input pair helps user to select the most putative interaction. The accessible segments between lncRNA and mRNA has been identified by using AccessE algorithm designed by us. The binding information among the accessible segments of lncRNA and its target can be visualized as well as downloaded.
### Prequisites
Ubuntu environment<br />
Python 2.7<br />
Anaconda<br />
Python 3.7<br />
LightGBM <br />
RNAstructure version 6.0 (64-bit), released on September 21, 2017.<br />


### How to Install and Run
1. Login to the system as root user
2. Download and Install PARASOR
    > git clone https://github.com/carushi/ParasoR
    > cd ParasoR
    > ./configure
    >  make
    >  make install
    >  autoreconf -ivf
3. Test installation was successful or not
    > cd script
    > sh check.sh
    > cat ../doc/pre.txt
    > python test.py
4. Download and Install RNAstructure 6.0
    Go to https://rna.urmc.rochester.edu/RNAstructure.html
    Download RNAstructure
    Need to be registered first
    Goto archived version
    Download RNAstructure 6.0 sep 21 2017;Command line interfaces;download 64bit-linux(53.71mb)
    >cd home/rootuser/ParasoR/script/
    >wget http://rna.urmc.rochester.edu/Releases/6.0/RNAstructureLinuxTextInterfaces64bit.tgz
    >tar -xvzf RNAstructureLinuxTextInterfaces64bit.tgz
    >cd RNAstructure
    >cp cal_hybrid.py . (Copy cal_hybrid.py inside RNAstructure)
5.  Install Anaconda3
    >wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
    *must be installed in non-root mode
    >sh *.sh
    >/home/user/anaconda3/
6.  Install LightGBM, Biopython and python 3.7
    >/home/user/anaconda3/bin/pip install lightgbm
    >/home/user/anaconda3/bin/pip install biopython
7.  Keep all the python (.py) and machine learning moel (.sav) files in 
    /home/user/ParasoR/script/ and cal_hybrid.py will be in RNAstructure/ only.
    >cp /home/user/ParasoR/script/Main.py .
    >cp /home/user/ParasoR/script/Extract_Feature.py .
    >cp /home/user/ParasoR/script/cal_modified_hybrid_energy1.py .
    >cp /home/user/ParasoR/script/cal_stem.py .
    >cp /home/user/ParasoR/script/count_base_v1.py .
    >cp /home/user/ParasoR/script/features_predict.py .
    >cp /home/user/ParasoR/script/basecount.py .
    >cp /home/user/ParasoR/script/Dataset_Generator.py .
    >cp /home/user/ParasoR/script/RNAstructure/cal_hybrid.py RNAstructure/.
    >cp /home/user/ParasoR/script/ML_Prediction.py .
    >cp /home/user/ParasoR/script/Predict_Binding.py .
    >cp /home/user/ParasoR/script/baggingPU.py .
    >cp /home/user/ParasoR/script/*.sav .
    >cp /home/user/ParasoR/script/query.fa .
    >cp /home/user/ParasoR/script/target.fa .
    >cp /home/user/ParasoR/script/max_base_span.txt .
    **EVERY call must be in root Mode
8.  Copy all the html and php files and supporting folders to 
    >/home/user/ParasoR/script/
    >cp /home/user/ParasoR/script/index_1.html .
    >cp /home/user/ParasoR/script/*.php .
    >cp -a /home/user/ParasoR/script/contactform/. contactform/
    >cp -a /home/user/ParasoR/script/img/. img/
    >cp -a /home/user/ParasoR/script/lib/. lib/
    >cp -a /home/user/ParasoR/script/css/. css/
    >cp -a /home/user/ParasoR/script/js/. js/
9.  link php to the server
    Softlink:
    >cd var/www/html
    >sudo ln -s /home/user/ParasoR/script/ TargetPrediction
    >sudo visudo
    >www-data ALL = (ALL) NOPASSWD:ALL
    >Defaults  !requiretty
10. To give permission to upload file from outside
    >cd /home/sibun/ParasoR/
    >sudo chown nobody *
    >sudo chmod -R 777 *
    
    

 

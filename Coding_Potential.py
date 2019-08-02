import os

if __name__ == "__main__":
	os.system("python /home/sibun/CPC2-beta/bin/CPC2.py -i query.fa -o cpc2_query.txt");
	os.system("python /home/sibun/CPC2-beta/bin/CPC2.py -i target.fa -o cpc2_target.txt");
	os.system("python /home/sibun/PLEK.1.2/PLEK.py -fasta query.fa -out plek_query.txt");
	os.system("python /home/sibun/PLEK.1.2/PLEK.py -fasta target.fa -out plek_target.txt");
	os.system("python /home/sibun/CPAT-1.2.4/bin/cpat.py -g target.fa -d /home/sibun/CPAT-1.2.4/dat/Human_logitModel.RData -x /home/sibun/CPAT-1.2.4/dat/Human_Hexamer.tsv -o cpat_target.txt");
	os.system("python /home/sibun/CPAT-1.2.4/bin/cpat.py -g query.fa -d /home/sibun/CPAT-1.2.4/dat/Human_logitModel.RData -x /home/sibun/CPAT-1.2.4/dat/Human_Hexamer.tsv -o cpat_query.txt");
	
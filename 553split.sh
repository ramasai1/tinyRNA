cat /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/genicregionremovedfasta/exon/SRR3279553.fa | paste - - | perl -ne '@x=split m/\t/; unshift @x, length($x[1]); print join "\t",@x;' | sort -n | cut -f2- | tr "\t" "\n" > /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/CEND_gregremoved_sortedfasta/exon/SRR3279553.fa


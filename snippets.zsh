snippet for 'for re'
for dir in `ls -F | grep '/$'`; do
        echo "Entering $dir"
        cd $dir
        command
        cd ..
done
endsnippet

snippet rm 'rm'
rm `ls | egrep -v 'POSCAR|POTCAR|INCAR|KPOINTS'`
endsnippet

snippet rm 'rm'
rm {CHG,CHGCAR,CONTCAR,DOSCAR,EIGENVAL,IBZKPT,OSZICAR,OUTCAR,PCDAT,REPORT,vasprun.xml,WAVECAR,XDATCAR}
endsnippet

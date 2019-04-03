# Calculate bottleneck distances 
# Usage: vmd -dispdev text -e bottleneck_extract.tcl
# 

#{{Xi1 Xi2 Bottleneck}}
set data { }
set dcdlist [lsort [glob *.dcd]]
set numdcdlist [llength $dcdlist]
for {set j 0} {$j < $numdcdlist} {incr j} {
    animate goto $j
    mol load psf gluk2-apo.psf dcd [lindex $dcdlist $j]
    set nf [molinfo top get numframes]
    for {set f 0} {$f < $nf} {incr f} {
        animate goto $f
        set r1 [atomselect top "segid PROT and resid 90 91 92 and not name H"]
        set s1 [atomselect top "segid PROT and resid 142 143 and not name H"]
        set com_r1 [measure center $r1 weight mass]
        set com_s1 [measure center $s1 weight mass]
        set xi1 [vecdist $com_r1 $com_s1]
        set r2 [atomselect top "segid PROT and ((resid 12 and name N CA C O) and (resid 13 14 and not name H))"]
        set s2 [atomselect top "segid PROT and resid 174 175 and not name H"]
        set com_r2 [measure center $r2 weight mass]
        set com_s2 [measure center $s2 weight mass]
        set xi2 [vecdist $com_r2 $com_s2]
        set tyrgamma [atomselect top "segid PROT and resid 61 and name CG"]
        set valgamma [atomselect top "segid PROT and resid 138 and name CG1"] 
        set com_tyrgamma [measure center $tyrgamma weight mass]
        set com_valgamma [measure center $valgamma weight mass]
        set bottleneckdist [vecdist $com_tyrgamma $com_valgamma]
        lappend data [list $xi1 $xi2 $bottleneckdist]
        $r1 delete
        $s1 delete
        $r2 delete
        $s2 delete
        $tyrgamma delete
        $valgamma delete
    }
    animate delete all 
animate delete all
mol delete all
}
mol delete all
set output [join $data \n]
set filename "gluk2_bottleneck_data.dat"
set writing [open $filename "w"]
puts -nonewline $writing $output
close $writing
llength $dcdlist

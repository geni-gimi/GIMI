#!/bin/bash

echo $1
echo ${1}.rdf

wget -O ~/Tutorials/GIMI/$1/${1}.rdf emmy9.casa.umass.edu/GEC15-GIMI-Tutorial/RDFs/${1}.rdf

wget -O ~/Tutorials/GIMI/common/step1-ping_all.rb emmy9.casa.umass.edu/GEC15-GIMI-Tutorial/scripts/step1-ping_all.rb
wget -O ~/Tutorials/GIMI/common/step2-routing.rb emmy9.casa.umass.edu/GEC15-GIMI-Tutorial/scripts/step2-routing.rb
wget -O ~/Tutorials/GIMI/common/step3-ping_e2e.rb emmy9.casa.umass.edu/GEC15-GIMI-Tutorial/scripts/step3-ping_e2e.rb
wget -O ~/Tutorials/GIMI/common/step4-otg_nmetrics.rb emmy9.casa.umass.edu/GEC15-GIMI-Tutorial/scripts/step4-otg_nmetrics.rb
wget -O ~/Tutorials/GIMI/common/system_monitor.rb emmy9.casa.umass.edu/GEC15-GIMI-Tutorial/scripts/system_monitor.rb
wget -O ~/Tutorials/GIMI/common/nmetrics_app.rb emmy9.casa.umass.edu/GEC15-GIMI-Tutorial/scripts/nmetrics_app.rb
wget -O ~/Tutorials/GIMI/common/R_script_ping.r emmy9.casa.umass.edu/GEC15-GIMI-Tutorial/scripts/R_script_ping.r
wget -O ~/Tutorials/GIMI/common/R_script_otr.r emmy9.casa.umass.edu/GEC15-GIMI-Tutorial/scripts/R_script_otr.r
wget -O ~/Tutorials/GIMI/common/R_script_nmetrics.r emmy9.casa.umass.edu/GEC15-GIMI-Tutorial/scripts/R_script_nmetrics.r
wget -O ~/Tutorials/GIMI/common/R_script_ping_e2e.r emmy9.casa.umass.edu/GEC15-GIMI-Tutorial/scripts/R_script_ping_e2e.r

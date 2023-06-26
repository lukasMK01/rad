# -*- coding: utf-8 -*-
"""
main program to create input files and bash scripts to run them

Lukas Monrad-Krohn: 24.05.2023
"""

# create a bash script that will contain the commands to run the model for each case
output_sh = open('./main_file.sh', 'w')


def cr_input(dati, rs_path, lat, lon, wvl=[320,950]):
    # prepare variables etc
    # create inputfile name
    name = 'test_libradtran'
    # longitude direction
    if lon < 0:
        dir_lon = 'W'
    else:
        dir_lon = 'E'
    
    # date and time
    yr = 
    with open (name+'.inp', 'w') as file:
        file.write('atmosphere_file /projekt_agmwend/home_rad/sophie/libradtran/atmmod/afglsw.dat \n')
        file.write(f'wavelength {wvl[0]} {wvl[1]}\n')
        file.write(f'radiosonde ../../radiosonden/selected_soundings/{rs_path} H2O RH \n')
        file.write(f'time {yr} {mo} {da}    {hh}    {mm}    {ss} \n')
        file.write(f'latitude N    {lat} \n')
        file.write(f'longitude {dir_lon}    {lon} \n')
        file.write('zout 0.00000 \n')
        file.write('albedo_file /projekt_agmwend/home_rad/sophie/libradtran/albedo/ac3/albedo_snow_spec.dat \n')
        file.write('mol_abs_param dsbdart \n')
        file.write('rte_solver disort \n')
        file.write('output_user lambda eglo \n')
        file.write('aerosol_default \n')
        file.write('aerosol_species_file maritime_clean \n')
        file.write('aerosol_set_tau_at_wvl 500 0.05 \n')
        file.write('quiet')
#!/usr/bin/python3

greek = ['Alpha','Beta','Gamma','Delta','Epsilon','Zeta','Eta','Theta','Iota','Kappa','Lambda','Mu','Nu','Xi','Omicron','Pi','Rho','Sigma final','Sigma','Tau','Upsilon','Phi','Chi','Psi','Omega']

for pos, cname in enumerate(greek, start=0x03B1):
    try:
        char = chr(pos)
        print(f"{pos:#x} {cname:<12s}: {char} {char.upper()}") 
        pos += 1 
    except UnicodeEncodeError as err: 
        print(cname, 'unknown')


from astropy.io import ascii
from astropy.table import Table
from tqdm import tqdm
import numpy as np

def main():
    print ("Performing query")
    tic, p0 = [], []
    for i in tqdm(range(1, 47)):
        vila = ascii.read(f"http://tessebs.villanova.edu/?order_by=tic&page={i}")
        tic.append(vila['TESS ID'])
        p0.append(vila['P0 [days]'])

    tic, p0 = np.array(tic), np.array(p0)
    vila_master = Table([np.concatenate(tic), np.concatenate(p0)], names=("TIC", 'period'))
    vila_master.write("EB_TESScat.ascii", format='ascii')
    print ("Query done!")

if __name__ == "__main__":
    main()
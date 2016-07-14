#!/usr/bin/env python
import tkinter
import astropy.coordinates as coord
from astropy import units as u

if __name__ == "__main__":
    coord.AltAz(alt=10 * u.degree, az=30 * u.degree)
    tkinter._test()

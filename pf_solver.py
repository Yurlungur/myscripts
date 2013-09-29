#!/usr/bin/env python2

# pf_solver.py
# Authors: Jonah Miller (jmille16@uoguelph.ca)
#          Katherine White (k22white@uwaterloo.ca)
# Time-stamp: <2013-09-29 03:38:43 (jonah)>

# This program solves for the Fermi momentum of a White Dwarf star as
# a function of the radius of the star. 
#
# Uses the shooting method and eighth-order adaptive Runge-Kutta for
# integration
#
# Uses the cumulative trapezoid rule for integration. We could
# implement this ourselves like we did Forward Euler, but we already
# implemented forward Euler and we felt lazy.

# Add modules
# ----------------------------------------------------------------------
from numpy import pi,abs,sqrt,array,arange # Mathematical tools
from scipy import integrate # Numerical integration tools
from matplotlib import pyplot as plt # Plotting tools
import warnings # To prevent extraneous warning messages
# ----------------------------------------------------------------------

# DEFINITIONS
# ----------------------------------------------------------------------

# pF is the Fermi momentum
# p_prime = d pF/dr
# r is the radius

# ----------------------------------------------------------------------

# Global Constants
# ----------------------------------------------------------------------

# Fundamental Constants

M_sun = 1.98855 * 10**30 # (kg). Mass of the sun.
R_sun = 6.963 * 10**8 # (m). Equatorial radius of the sun.
M_p = 1.672621777 * 10**(-27) # (kg). Mass of a proton.
M_e = 9.10938291 * 10**(-31) # (kg). Mass of an electron.
hbar = 1.054571726 * 10**(-34) # (J-s). Reduced Planck Constant
c = 299792458 # (m/s). Speed of light.
G = 6.67384 * 10**(-11) # N (m/kg)^2 # Newton's constant.

# Derived constants

# The average Fermi momentum in the sun. Used as a baseline for
# guesses for initial conditions.
pF_avg_sun = (3*(pi**2)*(hbar**3)*(M_sun/M_p)*(R_sun**(-3)))**(1./3)

# ----------------------------------------------------------------------


# Simulation Parameters
# ----------------------------------------------------------------------

p_prime_0 = 10**(-10) # (dpF/dr)(r=0).
dr = 0.5 * 10**(-4)*(0.04 * R_sun) # The change in r at each time step. 
r_0 = dr*10**(-20) # initial radius... i.e., the origin. The equation has a
                  # coordinate singularity here, so we have to be careful.
# A list of initial guesses for pF at the origin.
pF_0_guesses_1  = [0.28 * 10**(-21) * i for i in [0.5,1,1.5,2.0]]
pF_0_guesses_2 = 0.28 * 10**(-21) * arange(0.5,20.5,0.25)

# ----------------------------------------------------------------------


# Methods
# ------------------------------------- ---------------------------------
def f(r,pF,p_prime):
    """
    d(p_prime)/dr = - f(pF,p_prime,r).

    We have to be careful to use the correct formula at the
    origin. The most generally factored formula has a coordinate
    singularity. However, since we know that p_prime = 0, we can
    simplify things, which removes the coordinate singularity.
    """
    # A recurring term
    sum_term = c**2 * M_e**2 + pF**2

    if p_prime == 0: # The r=0 case when things are simpler.
        denominator = 3*pi*c*(hbar**3)
        f = (4 * G * M_p**2 * pF**2 * sqrt(sum_term))/float(denominator)

    else: # The global denominator of the expression
        denominator = 3*pi*c*(hbar**3)*r*pF*sum_term
        # The numerator of the expression
        numerator = 4*G*r*(M_p**2)*(pF**3)*(sum_term**(3./2.))\
            + 3*pi*c*(hbar**3)*p_prime*(c**2 * M_e**2 * r * p_prime\
                                            + 2 * c**2 * M_e**2 * pF + 2 * pF**3)
        # The term that we subtract from the old p_prime to generate the new one.
        f = float(numerator)/denominator

    return f

def new_p_prime(pF,p_prime,r):
    """
    Iterates the derivative of pF with respect to r.

    We have to be careful to use the correct formula at the
    origin. The most generally factored formula has a coordinate
    singularity. However, since we know that p_prime = 0, we can
    simplify things, which removes the coordinate singularity.
    """
    return p_prime - f(r,pF,p_prime)*dr

def new_pF(pF,p_prime):
    """
    Iterates pF with respect to r
    """
    return pF + p_prime*dr

def new_r(r):
    """
    Iterates r
    """
    return r + dr

def runge_kutta(pF_0,output=False):
    """
    Given an initial pF_0, tries to solve the ODE system. Stops
    integrating when pF=0.

    Returns three lists with itnegrated data: Fermi momentum,
    derivative of the Fermi momentum, and radius. All lists should be
    the same length.
    """
    # When to stop integration
    pF_s = pF_0/100.0 # pF at the surface of the star.


    # Parameter arrays
    pF = [pF_0]
    p_prime = [p_prime_0]
    r = [r_0]

    if output:
        print "r/R_sun\tpF\tp_prime"

    # Setup the ODE system. The system is
    # y = [pF,p_prime]
    # where y is a vector.
    # The solver expects y'(r) = f(r)
    # To set this up, we bind a local function y_prime. 
    def y_prime(r,y):
        pF = y[0]
        p_prime = y[1]
        return array([p_prime,-f(r,pF,p_prime)])

    # Similarly, we need to bind the initial conditions to a vector
    y_0 = array([pF_0,p_prime_0])

    # Setup the integrator, which is an object.
    integrator = integrate.ode(y_prime).set_integrator('dop853',dfactor=0.001,
                                                       nsteps=1,max_step=dr,
                                                       first_step=r_0/100.0)
    integrator.set_initial_value(y_0,r_0)

    # We need to surpress some error messages
    integrator._integrator.iwork[2]=-2
    warnings.filterwarnings("ignore",category=UserWarning)

    # Now we're ready for integration
    # Iterate with Runge-Kutta until pF hits pF_s. At
    # this point, we've hit the surface of the star.
    
    # Unfortunately, the integrator has bound its integration variable
    # to the letter t. This gets a little confusing... but hopefully
    # not too much.
    while integrator.y[0] > pF_s and integrator.t < R_sun:
        integrator.integrate(R_sun,step=True)
        pF.append(integrator.y[0])
        p_prime.append(integrator.y[1])
        r.append(integrator.t)

        if output:
            print "{}\t{}\t{}".format(r[-1]/R_sun,pF[-1],p_prime[-1])

    # We want to prune the output so that pF has no negative values.
    if pF[-1] < 0:
        pF[-1] = 0

    # We have to let the warnings return to their previous state.
    warnings.resetwarnings()

    return pF,p_prime,r


def forward_euler(pF_0,output=False):
    """
    Given an initial pF_0, tries to solve the ODE system. Stops
    integrating when pF=0.

    Returns three lists with itnegrated data: Fermi momentum,
    derivative of the Fermi momentum, and radius. All lists should be
    the same length.
    """
    # Parameter arrays
    pF = [pF_0]
    p_prime = [p_prime_0]
    r = [r_0]

    # When to stop integration
    pF_s = pF_0/1000. # pF at the surface of the star.

    if output:
        print "r/R_sun\tpF\tp_prime"

    # Iterate with first-order forward Euler until pF hits pF_s. At
    # this point, we've hit the surface of the star.
    while pF[-1] > pF_s and r[-1] < R_sun:
        p_prime.append(new_p_prime(pF[-1],p_prime[-1],r[-1]))
        pF.append(new_pF(pF[-1],p_prime[-1]))
        r.append(new_r(r[-1]))

        if output:
            print "{}\t{}\t{}".format(r[-1]/R_sun,pF[-1],p_prime[-1])

        # We want to prune the output so that pF has no negative values.
        if pF[-1] < 0:
            pF[-1] = 0

    return pF,p_prime,r

def shoot(pF_0_guess_list=pF_0_guesses_1,algorithm=runge_kutta,testing = False):
    """
    Tries Forward Euler with the initial guesses for pF_0 defined in
    the simulation parameters. Returns a list of the results.
    """
    # Initial parameters
    pF_list = []
    p_prime_list = []
    r_list = []

    for pF_0 in pF_0_guess_list:
        print "Trying initial guess: {} kg m/s".format(pF_0)
        pF,p_prime,r = algorithm(pF_0,testing)
        pF_list.append(pF)
        p_prime_list.append(p_prime)
        r_list.append(r)
    return pF_list,p_prime_list,r_list

def plot_pF(r_list,pF_list):
    """
    Plots one solution
    """

    # Ensure type is correct
    if type(pF_list[0]) != list:
        pF_list = [pF_list]
    if type(r_list[0]) != list:
        r_list = [r_list]

    # Change the x-axis scale.
    for i in range(len(r_list)):
        r_list[i] = array(r_list[i])
        r_list[i] /= R_sun

    # Plot it.
    lines = [plt.plot(r_list[i],pF_list[i]) for i in range(len(r_list))]
    plt.xlabel(r'radius $(R/R_{sun})$')
    plt.ylabel(r'Fermi Momentum $(kg m/s)$')
    #    plt.axis([0,7,-0.05,1.05])
    plt.title("Fermi Momentum as a Function of Radius")
    plt.show()
    return

def find_mass(r,pF):
    """
    Integrates pF as a function of r to get the mass of the star.
    """
    # Our input values MUST be numpy arrays. Otherwise power laws
    # don't work properly.
    r = array(r)
    pF = array(pF)

    # We multiply this by our integral when we're done
    prefactor = 4*M_p/(3*pi*(hbar**3))
    # This is the integrand
    integrand = r**2 * pF**3
    # And the integral:
    integral = integrate.simps(integrand,r)
    return prefactor*integral
    
    

# ----------------------------------------------------------------------

def make_characteristic_pF_plots(pF_0_guess_list=pF_0_guesses_1):
    pF_list,p_prime_list,r_list = shoot(pF_0_guess_list)
    masses = [find_mass(r_list[i],pF_list[i])/M_sun for i in range(len(r_list))]
    radii = [r[-1]/R_sun for r in r_list]
    plot_pF(r_list,pF_list)
    print "R/R_sun\tM/M_sun"
    for i in range(len(masses)):
        print "{}\t{}".format(radii[i],masses[i])
    return

def make_plot_of_mass_vs_radius(pF_0_guess_list=pF_0_guesses_2):
    pF_list,p_prime_list,r_list = shoot(pF_0_guess_list)
    masses = [find_mass(r_list[i],pF_list[i])/M_sun for i in range(len(r_list))]
    radii = [r[-1]/R_sun for r in r_list]
    plot_pF(r_list,pF_list)
    plt.plot(radii,masses)
    plt.xlabel(r'Radius $(R/R_{sun})$')
    plt.ylabel(r'Mass $(M/M_{sun})$')
    plt.title("Mass as a Function of Radius\nAnd the Chandrasekhar Limit")
    plt.show()
    print "R/R_sun\tM/M_sun"
    for i in range(len(masses)):
        print "{}\t{}".format(radii[i],masses[i])
    return

main = make_plot_of_mass_vs_radius

# If the program is loaded as a module, this prevents it from running the main loop.
if __name__ == "__main__":
    main()


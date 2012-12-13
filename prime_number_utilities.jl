# Author: Yurlungur
# ----------------------------------------------------------------------



# Bounds on primes > 6. Given by the prime number theorem. For values
# <= 6, gives the exact answer.
# ----------------------------------------------------------------------
# An upper bound on the nth prime number.
function prime_upper_bound(x::Int)
    if x <= 6; return max(filter((i)->i<=x,[2,3,5])); end
    return floor(x*(log(x) + log(log(x))))
end
# A lower bound on the nth prime number.
function prime_lower_bound(x::Int)
    if x <= 6; return max(filter((i)->i<=x,[2,3,5])); end
    return floor(x*(log(x) + log(log(x)) - 1))
end

# My solution uses the Sieve of Eratosthenes.
# Re-implimented to be faster.
# Return a list of all primes below N.
function sieve_of_eratosthenes(N::Int)
    # Each index>2 indicates a number that could be prime. I waste the
    # first element of the array. Less of a headache.
    factors::Array{Bool} = trues(N)
    # Iterate through all values. If they're prime, add them to the
    # sum and remove their multiples.
    for i::Int=2:floor(sqrt(N))
        if factors[i]
            let j::Int = i^2; while j <= N
                factors[j] = false
                j += i
            end; end
        end
    end
    return filter((x)->factors[x],[2:N])
end


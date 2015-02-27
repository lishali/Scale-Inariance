Scale-Inariance
===============

We briefly explore the conjecture that real road networks have the property that the ratio between the geodesic distance and road distance between any two points is scale invariant.  That is, no matter how close or far apart two points are, they enjoy the same ratio between their geodesic and road network distances.

=======
We take various datasets that would be a good approximation of choosing uniformly at random from the population of residential addresses.  Note that it s not enough to sample lat-long, or zipcodes at random since they do not represent the distribution of residential address.  In the case of zipcodes, for instance, choosing uniforming at random in the set of zipcodes is a distribution that favours well connected points of the road network (zipcodes are usually traced by various maps API to mail centers, which are situated in more accessible parts of cities and towns).   

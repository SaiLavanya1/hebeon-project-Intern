mean = ages.mean()
dists = ages-mean
dists = dists*dists
summed_dists = np.sum(dists) 
avg_dist = summed_dists/len(ages) 
std_dev = np.sqrt(avg_dist) 
print(std_dev)

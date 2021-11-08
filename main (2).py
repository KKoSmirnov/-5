def medians(nums1, nums2):
    comb_nums = nums1 + nums2
    comb_nums = sorted(comb_nums)
    length = int(len(comb_nums))
    if len(comb_nums) % 2 == 1:
        median = comb_nums[length/2-0.5]
    else:
        median = (comb_nums[int(length/2)]+comb_nums[int(length/2-1)])/2
    return "%.5f" % median

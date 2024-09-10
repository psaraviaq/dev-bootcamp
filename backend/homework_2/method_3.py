import timeit

original_list = list(range(10000000))
copy_timings = []

for i in range(10):

    #! ------------ START ---------------
    start_copy = timeit.default_timer()
    copy_list = [*original_list]            #* [*list]
    end_copy = timeit.default_timer()
    #! ------------- END ----------------

    #* Storing time
    copy_time = end_copy - start_copy
    copy_timings.append(copy_time)


#* -------- Printing Times --------
print("\n---------------------------                    [*list]                   --------------------------------")
print("\n     " + "     |     ".join(str(t+1) for t in range(10)))
print("-"*120)
print("  " + "  |  ".join(f"{t:.5f}" for t in copy_timings))

#* -------- Average Time --------
avg_execution = sum(copy_timings) / len(copy_timings)
print(f"\nAverage time: {avg_execution:.5f}")
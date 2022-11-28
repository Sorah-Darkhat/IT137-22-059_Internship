from Solve_EoS import *
import concurrent.futures
import time

#if __name__ == '__main__':
#    for Ids in range(200):
#        st = time.time()
#        #Random_Seed = rd.randint(1,100)
#        #print("Random_Seed =",Random_Seed)
#        print(f"Id = [{10*Ids}-{10*Ids+9}]")
#        Count = 0
#        with concurrent.futures.ProcessPoolExecutor() as executor:
#            results= [executor.submit(Solve_EoS,Id = 10*Ids+i, , Ran = False, Random_Seed = Random_Seed) for i in range(10)]
#            for f in concurrent.futures.as_completed(results):
#                Count+=1
#                print(f"Number of Processes Completed {Count} out of {48} in {round((time.time()-st)/60,1)}m", end="\n")
                

if __name__ == '__main__':
    for r in range(2):
        st = time.time()
        Random_Seed = rd.randint(1,100)
        print("Random_Seed =",Random_Seed)
        Count = 0
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results= [executor.submit(Solve_EoS, Id = i, Ran = True, Random_Seed = Random_Seed) for i in range(48)]
            for f in concurrent.futures.as_completed(results):
                Count+=1
                print(f"Number of Processes Completed {Count} out of {48} in {round((time.time()-st)/60,1)}m", end="\n")
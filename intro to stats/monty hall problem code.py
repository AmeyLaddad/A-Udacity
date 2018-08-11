from random import randint

N = 1000

def simulate(N):
    k = 0
    for i in range(N):
        car_door = randint(1,3)
        my_guess = randint(1,3)
        
        if car_door == my_guess:
            m_door = randint(1,3)
            while m_door == car_door:
                m_door = randint(1,3)
        else:
            m_door = 6 - car_door - my_guess
        
        my_second_guess = 6 - my_guess - m_door
        if my_second_guess == car_door:
            k+= 1

    return float(k) / float(N)

print simulate(N)

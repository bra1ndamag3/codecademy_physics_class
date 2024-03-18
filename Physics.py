train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  print(c_temp)
f100_in_c = f_to_c(100)
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) +32
  print(f_temp)
c0_in_f = c_to_f(0)
def get_force(train_mass, train_acceleration):
  train_force = train_mass * train_acceleration
  return train_force

print('The GE train supplies ' + str(get_force(train_mass, train_acceleration)) + ' Newtons of force')
def get_energy(mass, c = 3*10**8):
  energy = mass * (c**2)
  return energy
print('A 1kg bomb supplies ' + str(get_energy(bomb_mass)) + ' Joules')

def get_work(mass, acceleration, distance):
  train_work = get_force(train_mass, train_acceleration) * distance
  return train_work
print('The GE train does ' + str(get_work(train_mass, train_acceleration, train_distance)), 'Joules of work over ' + str(train_distance) + ' meters')

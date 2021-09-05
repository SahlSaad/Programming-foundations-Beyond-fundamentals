# Debugging Challenge 
# Task : fix errors of this this code :

# def plant_recommendation(care):
#     if care = 'low':
#         print('aloe')
#     elif care == 'medium':
#         print('pothos')
#     elif care == 'medium':
#         print('orchid')

# plant_rec('low')
# plant_recommendation('medium')
# plant_recommendation('high')

# fix line number 5: == not = ,
#  line number 12 plant_recommendation not plant_rec,
#  line number 9 high not medium

def plant_recommendation(care):
    if care == 'low':
        print('aloe')
    elif care == 'medium':
        print('pothos')
    elif care == 'high':
        print('orchid')

plant_recommendation('low')
plant_recommendation('medium')
plant_recommendation('high')


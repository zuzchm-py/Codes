import random

def tips():
    elements = ['The bicycle is the most energy-efficient means of transport, it is fast and keeps you fit.',
                'Do not throw garbage in the street, in addition to polluting, it clogs the ducts and can cause flooding.',
                'Is it really necessary to leave the light on in the living room? Always ask yourself this question: there are times when sunlight is enough to light up the entire living room. Use electric light only on very dark days or when it is really necessary.',
                'By sharing your car, we reduce the use of gasoline, a fossil fuel that causes climate change.',
                'Traditional light bulbs use a lot of electricity generating heat, use LED bulbs, you reduce energy consumption by 80%.']
    random_tip = ""

    
    random_tip += random.choice(elements)

    return random_tip

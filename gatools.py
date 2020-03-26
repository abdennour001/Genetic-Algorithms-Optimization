import enum
import numpy as np


class Category(enum.Enum):
    """
    This class represent the category type.

    Attributes:
        TOP (int): the category TOP.
        BOTTOM (int): the category BOTTOM.
        SHOES (int): the category SHOES.
        NECK (int): the category NECK.
        HANDBAG (int): the category HANDBAG.
    """
    TOP      = 1000
    BOTTOM   = 2000
    SHOES    = 3000
    NECK     = 4000
    HANDBAG  = 5000

class Color(enum.Enum):
    """
    This class represent the color type.
    
    Attributes:
        DARK (int): dark color.
        BRIGHT (int): bright color.
    """
    DARK    = 1
    BRIGHT  = 2

class DressCode(enum.Enum):
    """
    This class is the dress code type.

    Attributes:
        CAUSAL (int): the casual dress code.
        SPORTSWEAR (int): the sportswear dress code.
        BUSINESS (int): the business dress code.
        EVENING (int): the evening dress code.

    """
    CASUAL      = 1
    SPORTSWEAR  = 2
    BUSINESS    = 3
    EVENING     = 4

class Piece(enum.Enum):
    """
    TOP
    """
    T__SHIRT            = 1001
    BLOUSE              = 1002
    BODYSUIT            = 1003
    SLEEVELESS          = 1004
    TANK                = 1005
    SWEATER             = 1006
    VEST                = 1007
    BLAZER              = 1008
    JACKET              = 1009
    HOODIE              = 1010
    CARDIGAN            = 1011

    """
    BOTTOM
    """
    JEANS               = 2001
    KNEE_LENGTH_PANT    = 2002
    ANKLE_LENGTH_PANT   = 2003
    HIGHT_WAIST_PANTS   = 2004
    LEGGING             = 2005
    SWEATPANTS          = 2006
    WIDE_LEG_PANTS      = 2007
    MAXI_SKIRT          = 2008
    MIDI_SKIRT          = 2009
    SHORT_SKIRT         = 2010

    """
    SHOES
    """
    SANDALS             = 3001
    SNEAKERS            = 3002
    HIGHT_HEEL          = 3003
    MID_HEEL            = 3004
    LOW_HEEL            = 3005
    FLAT                = 3006
    BOOTS               = 3007

    """
    NECK
    """
    NECKLACE            = 4001
    CHOKER              = 4002
    SCARF               = 4003
    TIE                 = 4004
    BOW_TIE             = 4005

    """
    HANDBAG
    """
    BACKPACK            = 5001
    PURSE               = 5002
    CLUTCH              = 5003
    BELT_BAG            = 5004
    CROSS_BAG           = 5005

class DataTable:
    """
    This class contains our data which is represented in the table.
    DataTable.data[Category][Piece]
                                |
                                |-> color
                                |-> dress-code
                                |-> price

    Attributes:
        data (dict): It contains all the data in a dictionary.

    """

    top_dict = {
        Piece.T__SHIRT : {
            'color': [
                Color.DARK,
                Color.BRIGHT
            ],
            'dress-code': [
                DressCode.CASUAL,
                DressCode.SPORTSWEAR
            ],
            'price': 0.0
        },
        Piece.BLOUSE : {
            'color': [Color.BRIGHT],
            'dress-code': [
                DressCode.BUSINESS,
                DressCode.EVENING
            ],
            'price': 200.0
        },
        Piece.BODYSUIT : {
            'color': [Color.DARK],
            'dress-code': [
                DressCode.CASUAL,
                DressCode.EVENING
            ],
            'price': 150.0
        },
        Piece.SLEEVELESS : {
            'color': [Color.DARK],
            'dress-code': [DressCode.CASUAL],
            'price': 150.0
        },
        Piece.TANK : {
            'color': [Color.BRIGHT],
            'dress-code': [
                DressCode.CASUAL,
                DressCode.SPORTSWEAR
            ],
            'price': 70.0
        },
        Piece.SWEATER : {
            'color': [Color.DARK],
            'dress-code': [
                DressCode.CASUAL,
                DressCode.BUSINESS
            ],
            'price': 200.0
        },
        Piece.VEST : {
            'color': [Color.DARK],
            'dress-code': [DressCode.BUSINESS],
            'price': 300.0
        },
        Piece.BLAZER : {
            'color': [Color.DARK],
            'dress-code': [DressCode.BUSINESS],
            'price': 430.0
        },
        Piece.JACKET : {
            'color': [Color.BRIGHT],
            'dress-code': [DressCode.CASUAL],
            'price': 0.0
        },
        Piece.HOODIE : {
            'color': [
                Color.DARK,
                Color.BRIGHT
            ],
            'dress-code': [DressCode.SPORTSWEAR],
            'price': 230.0
        },
        Piece.CARDIGAN : {
            'color': [Color.BRIGHT],
            'dress-code': [DressCode.CASUAL],
            'price': 300.0
        },
    }

    bottom_dict = {
        Piece.JEANS : {
            'color': [Color.DARK],
            'dress-code': [DressCode.CASUAL],
            'price': 150.0
        },
        Piece.KNEE_LENGTH_PANT : {
            'color': [Color.BRIGHT],
            'dress-code': [DressCode.CASUAL],
            'price': 220.0
        },
        Piece.ANKLE_LENGTH_PANT : {
            'color': [Color.DARK],
            'dress-code': [DressCode.BUSINESS],
            'price': 0.0
        },
        Piece.HIGHT_WAIST_PANTS : {
            'color': [Color.BRIGHT],
            'dress-code': [DressCode.BUSINESS],
            'price': 150.0
        },
        Piece.LEGGING : {
            'color': [Color.DARK],
            'dress-code': [DressCode.CASUAL],
            'price': 100.0
        },
        Piece.SWEATPANTS : {
            'color': [Color.BRIGHT],
            'dress-code': [DressCode.CASUAL],
            'price': 100.0
        },
        Piece.WIDE_LEG_PANTS : {
            'color': [
                Color.DARK,
                Color.BRIGHT
            ],
            'dress-code': [
                DressCode.BUSINESS,
                DressCode.EVENING
            ],
            'price': 500.0
        },
        Piece.MAXI_SKIRT : {
            'color': [Color.BRIGHT],
            'dress-code': [DressCode.EVENING],
            'price': 150.0
        },
        Piece.MIDI_SKIRT : {
            'color': [Color.DARK],
            'dress-code': [DressCode.BUSINESS],
            'price': 150.0
        },
        Piece.SHORT_SKIRT : {
            'color': [Color.BRIGHT],
            'dress-code': [DressCode.CASUAL],
            'price': 400.0
        },
    }

    shoes_dict = {
        Piece.SANDALS : {
            'color': [Color.DARK],
            'dress-code': [
                DressCode.CASUAL,
                DressCode.EVENING
            ],
            'price': 120.0
        },
        Piece.SNEAKERS : {
            'color': [Color.BRIGHT],
            'dress-code': [
                DressCode.SPORTSWEAR,
                DressCode.CASUAL
            ],
            'price': 300.0
        },  
        Piece.HIGHT_HEEL : {
            'color': [Color.DARK],
            'dress-code': [DressCode.EVENING],
            'price': 0.0
        },
        Piece.MID_HEEL : {
            'color': [Color.BRIGHT],
            'dress-code': [
                DressCode.CASUAL,
                DressCode.BUSINESS
            ],
            'price': 400.0
        },
        Piece.LOW_HEEL : {
            'color': [Color.DARK],
            'dress-code': [DressCode.BUSINESS],
            'price': 150.0
        },
        Piece.FLAT : {
            'color': [Color.BRIGHT],
            'dress-code': [DressCode.CASUAL],
            'price': 0.0
        },
        Piece.BOOTS : {
            'color': [Color.DARK],
            'dress-code': [DressCode.CASUAL],
            'price': 500.0
        },
    }

    neck_dict = {
        Piece.NECKLACE : {
            'color': [Color.DARK],
            'dress-code': [
                DressCode.EVENING,
                DressCode.BUSINESS
            ],
            'price': 150.0
        },
        Piece.CHOKER : {
            'color': [Color.BRIGHT],
            'dress-code': [
                DressCode.CASUAL,
                DressCode.EVENING
            ],
            'price': 0.0
        },
        Piece.SCARF : {
            'color': [Color.BRIGHT],
            'dress-code': [DressCode.CASUAL],
            'price': 250.0
        },
        Piece.TIE : {
            'color': [Color.DARK],
            'dress-code': [DressCode.BUSINESS],
            'price': 100.0
        },
        Piece.BOW_TIE : {
            'color': [Color.DARK],
            'dress-code': [DressCode.BUSINESS],
            'price': 100.0
        },
    }

    handbag_dict = {
        Piece.BACKPACK : {
            'color': [Color.BRIGHT],
            'dress-code': [DressCode.SPORTSWEAR],
            'price': 100.0
        },
        Piece.PURSE : {
            'color': [Color.BRIGHT],
            'dress-code': [DressCode.BUSINESS],
            'price': 600.0
        },
        Piece.CLUTCH : {
            'color': [Color.DARK],
            'dress-code': [DressCode.EVENING],
            'price': 500.0
        },
        Piece.BELT_BAG : {
            'color': [Color.DARK],
            'dress-code': [DressCode.CASUAL],
            'price': 300.0
        },
        Piece.CROSS_BAG : {
            'color': [Color.DARK],
            'dress-code': [DressCode.BUSINESS],
            'price': 0.0
        },
    }

    data = {
        Category.TOP : top_dict,
        Category.BOTTOM : bottom_dict,
        Category.SHOES : shoes_dict,
        Category.NECK : neck_dict,
        Category.HANDBAG : handbag_dict,
    }


class Outfit:
    """
    This is a class that represent our chromosome, it is the outfit that we need to optimize.
    The chromosome is encoded in an array like this : 
    chromosome == [(TOP piece), (BOTTOM piece), (SHOES piece), (NECK piece), (HANDBAG piece)].

    Attributes: 
        top (Category): The piece from the TOP category.
        bottom (Category): The piece from the BOTTOM category.
        shoes (Category): The piece from the SHOES category.
        neck (Category): The piece from the NECK category.
        handbag (Category): The piece from the HANDBAG category.

    """

    def __init__(self, top=Piece.T__SHIRT, bottom=Piece.JEANS, shoes=Piece.SANDALS, neck=Piece.NECKLACE, handbag=Piece.BACKPACK):
        """

        """
        self._top            = top
        self._bottom         = bottom
        self._shoes          = shoes
        self._neck           = neck
        self._handbag        = handbag

        # final representation : Binary encoding of genetic algorithm.
        # our chromosome will be encoded in a string of 0's and 1's.
        # we will use numpy arrays so the manipulation of those strings is easier.
        #self._chromosome     = np.array(['0' for _ in range(Outfit.chrom_length)])

    # getter of top
    @property
    def top(self):
        return self._top

    # setter of top
    @top.setter
    def top(self, top):
        self._top = top

    # getter of bottom
    @property
    def bottom(self):
        return self._bottom

    # setter of bottom
    @bottom.setter
    def bottom(self, bottom):
        self._bottom = bottom

    # getter of shoes
    @property
    def shoes(self):
        return self._shoes

    # setter of shoes
    @shoes.setter
    def shoes(self, shoes):
        self._shoes = shoes

    # getter of neck
    @property
    def neck(self):
        return self._neck

    # setter of neck
    @neck.setter
    def neck(self, neck):
        self._neck = neck

    # getter of handbag
    @property
    def handbag(self):
        return self._handbag

    # setter of handbag
    @handbag.setter
    def handbag(self, handbag):
        self._handbag = handbag


    def budgetVsSum(self, x):
        return x / (100 + x)


    def dressCodeFitness(self, dressCode):
        count = 0
        if dressCode in DataTable.top_dict[self._top]['dress-code']:
            count += 1
        if dressCode in DataTable.bottom_dict[self._bottom]['dress-code']:
            count += 1
        if dressCode in DataTable.shoes_dict[self._shoes]['dress-code']:
            count += 1
        if dressCode in DataTable.neck_dict[self._neck]['dress-code']:
            count += 1
        if dressCode in DataTable.handbag_dict[self._handbag]['dress-code']:
            count += 1

        fitness = count / len(Category)
        #print('dressCode fitness : {}'.format(fitness))
        return fitness

    def budgetFitness(self, budget):
        sum = DataTable.top_dict[self._top]['price'] + DataTable.bottom_dict[self._bottom]['price'] + DataTable.shoes_dict[self._shoes]['price'] + DataTable.neck_dict[self._neck]['price'] + DataTable.handbag_dict[self._handbag]['price']
        if sum > budget:
            return 0
        else:
            #print('budget fitness : {}'.format(self.budgetVsSum(budget - sum)))
            return self.budgetVsSum(budget - sum)


    def colorPalletFitness(self, color):
        count = 0
        if color in DataTable.top_dict[self._top]['color']:
            count += 1
        if color in DataTable.bottom_dict[self._bottom]['color']:
            count += 1
        if color in DataTable.shoes_dict[self._shoes]['color']:
            count += 1
        if color in DataTable.neck_dict[self._neck]['color']:
            count += 1
        if color in DataTable.handbag_dict[self._handbag]['color']:
            count += 1

        fitness = count / len(Category)
        #print('color fitness : {}'.format(fitness))
        return fitness


    def fitness(self, dressCode, color, budget):
        """
        This is the function that will return the fitness of our Outfit.

        Parameters:
            dressCode (DressCode): The dress code.
            color (Color): The color.
            budget (float): Our budget.

        Returns:
            fitness (float): A value between 0 and 1 represent this outfit's fitness, the close to 1 the better.

        """

        # declare our weights : w1 = 2/5, w2 = 2/5 and w3 = 1/5 where w1 and w2 are associated to dress code and budget and w3 for the color.
        w = [
            0.4,
            0.4,
            0.2
        ]

        fitness = w[0]*self.dressCodeFitness(dressCode) + w[1]*self.budgetFitness(budget) + w[2]*self.colorPalletFitness(color)

        return fitness

    def __repr__(self):
        return "<{}, {}, {}, {}, {}>".format(
            self.top.name.lower().replace('__', '-').replace('_', ' '), 
            self.bottom.name.lower().replace('_', ' '), 
            self.shoes.name.lower().replace('_', ' '), 
            self.neck.name.lower().replace('_', ' '), 
            self.handbag.name.lower().replace('_', ' ')
            )

if __name__ == '__main__':
    p = Outfit(top=Piece.SLEEVELESS, bottom=Piece.LEGGING, shoes=Piece.SANDALS, neck=Piece.CHOKER, handbag=Piece.BELT_BAG)
    print(p.fitness(DressCode.CASUAL, Color.DARK, 1.0))
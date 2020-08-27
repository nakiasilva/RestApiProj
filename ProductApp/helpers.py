# Helper Function used in Views

def loadProductDetails(self, querySet):
    '''
        Creates and return the product object in the desired format
    '''
    response_items = {}
    response_items['Items'] = []
    for item in querySet:
            contains = {}
            contains['Id'] = item.id
            contains['Name'] = item.name
            contains['Description'] = item.description
            contains['Price'] = item.price
            contains['DeliveryPrice'] = item.deliveryPrice
            response_items['Items'].append(contains)
    return response_items


def loadProductOptionDetails(self, querySet):
    '''
        Creates and return the product options object in the desired format
    '''
    response_items = {}
    response_items['Items'] = []
    for item in querySet:
            contains = {}
            contains['Id'] = item.id
            contains['Name'] = item.name
            contains['Description'] = item.description
            response_items['Items'].append(contains)
    return response_items


def validateObject(validKeys, data, check_all = False):
    is_valid = True

    val = [False for key in validKeys if data.get(key) == None]

    if check_all:
        if False in val:
            is_valid = False
    else:
        if len(val) == len(validKeys):
            is_valid = False
    
    return is_valid


# Easy to manage Error Messages

def success_code(id):
    lable = 'Message'
    code_dict = {
        1 : {
            lable : 'Item Successfully Added'
        },
        2 : {
            lable : 'Item Successfully Updated'
        },
        3 : {
            lable : 'Item Successfully Deleted'
        }
    }

    return code_dict[id][lable]


def error_code(id):
    lable = 'Error'
    code_dict = {
        1 : {
            lable : 'Item cannot be added, check payload'
        },
        2 : {
            lable : 'Item cannot be updated, check payload'
        },
        3 : {
            lable : 'Item cannot be deleted. Not Found.'
        },
        4 : {
            lable : 'Item cannot be added. Not Found.'
        },
        5 : {
            lable : 'Item cannot be updated. Not Found.'
        },
        6 : {
            lable : 'Invalid Request'
        },
        7 : {
            lable : 'Item Not Found.'
        },
        8 : {
            lable : 'Name Not Found.'
        }
    }
    return code_dict[id][lable]
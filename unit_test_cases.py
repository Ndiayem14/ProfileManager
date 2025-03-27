def test_saveprofile():
    '''
    we are testing the save_profile function
    '''
# Testing the save profile function
    name_entry = "Sotaire"
    age_entry = "25"
    gender_entry = "M"
    occupation_entry = "S"

    with open('profiles.txt',
              'r') as info:
        line = info.readline()
        content = line.split(",")
        assert content[0].strip() == name_entry
        assert content[1].strip() == age_entry
        assert content[2].strip() == gender_entry
        assert content[3].strip() == occupation_entry
        line = info.readline()
        content = line.split(",")
        assert content[0].strip() == 'Moise'
        assert content[1].strip() == '30'
        assert content[2].strip() == 'binary'
        assert content[3].strip() == 'programmer'

def main():
    test_saveprofile()



main()
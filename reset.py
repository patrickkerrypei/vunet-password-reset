import requests
session = requests.Session()


def login(vunet_id, vunet_password):

    print '\nLogging in...'
    print '\t{:11}:\t{}'.format('[ID]', vunet_id)
    print '\t{:11}:\t{}\n'.format('[Password]', vunet_password)
    url = 'https://jprod.its.vanderbilt.edu/apps3/idm/user/login.jsp?lang=en&cntry=US'
    payload = {
        'id': '',
        'command': 'login',
        'activeControl': '',
        'accountId': vunet_id,
        'password': vunet_password
    }

    response = session.post(url, data=payload)

    if 'Error' not in response.text:
        print '[Login]: {}'.format('Success')
    else:
        print '[Login]: Failure / Incorrect Credentials'
        exit(1)


def change_password(new_password, iteration):
    url = 'https://jprod.its.vanderbilt.edu/apps3/idm/user/changePassword.jsp?lang=en&cntry=US'
    payload = {
        'id': '',
        'command': 'Save',
        'activeControl': '',
        'resourceAccounts.password': new_password,
        'resourceAccounts.confirmPassword': new_password
    }

    session.post(url, data=payload)

    print '[Password change #{:2}]: "{}"'.format(iteration, new_password)


def main():
    vunet_id = raw_input('Enter your VUNet ID: ')
    vunet_password = raw_input('Enter your password: ')

    login(vunet_id, vunet_password)

    base = 'abcABC123~'
    for i in range(10):
        change_password(base + str(i), i + 1)
    change_password(vunet_password, 11)

    print '\nCompleted password cycling. Your password is still: {}'.format(vunet_password)


if __name__ == '__main__':
    main()

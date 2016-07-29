from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests


class TeamcityWebGui(object):
    def __init__(self, teamcityURL, username, password):
        """
        Teamcity WEB GUI object
        :param teamcityURL: e.g. https://teamcity.example.com
        :param username: user name with admin permission
        :param password:
        """

        self.teamcityURL = teamcityURL
        self.username = username
        self.password = password
        self.cookie = ''
        self.__login()

    def __login(self):
        """
        Get cookies
        """
        driver = webdriver.Firefox()
        try:
            print("DEBUG - try login to Teamcity")
            driver.get("{}/login.html".format(self.teamcityURL))
            username = driver.find_element_by_id("username")
            username.send_keys(username)
            password = driver.find_element_by_id("password")
            password.send_keys(password)
            password.send_keys(Keys.RETURN)
            time.sleep(3)

            allCookies = driver.get_cookies()
            self.cookie = dict(map(lambda x: (x['name'], x['value']), allCookies))

            r = requests.get('{}'.format(self.teamcityURL), cookies=self.cookie)
            r.raise_for_status()
            print("DEBUG - logged OK")
        finally:
            driver.quit()

    def moveBuildType(self, buildConfigurationId, toProjectId):
        """
        Move build configuration to other project
        :param buildConfigurationId: Visible ID
        :param toProjectId: ID project
        """
        internalTCId = self.__configuration_getValue(buildConfigurationId, 'internalId', '')
        print('INFO - move {} [{}] to {}'.format(buildConfigurationId, internalTCId, toProjectId))

        moveData = {
            '-ufd-teamcity-ui-projectId': '',
            'projectId': toProjectId,
            'moveBuildType': 'Move',
            'buildTypeId': internalTCId,
            'sourceProjectId': ''
        }
        r = requests.post('{}/admin/moveBuildType.html'.format(self.teamcityURL),
                          cookies=self.cookie,
                          data=moveData,
                          headers={'Content-Type': 'application/x-www-form-urlencoded'}, )

        r.raise_for_status()
        print("INFO - moved")

    def __configuration_getValue(self, conf_id, type_str, var_name):
        """
        Get teamcity parameter
        """
        print(
            'configuration [{}] GET [{}] = '.format(conf_id, var_name),
            end='',
        )

        time.sleep(3)

        r = requests.get(
            self.__add_auth_to_url(
                self.teamcityURL + '/httpAuth/app/rest/buildTypes/id:{}/{}/{}'.format(conf_id, type_str, var_name),
                self.username, self.password),
            headers={'Content-Type': 'text/plain'},
            verify=False,
        )

        r.raise_for_status()

        value = r.text

        print('{!r}'.format(value))

        return value

    def __add_auth_to_url(self, url_str, login_str, pass_str):
        """
        Add username:password to URL
        """
        i = url_str.find('//')

        if i == -1:
            raise Exception("Can't detect http(s):// part of url: {}".format(url_str))

        return '{}//{}:{}@{}'.format(
            url_str[: i],
            login_str,
            pass_str,
            url_str[i + 2:],
        )

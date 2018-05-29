import os
import unittest

import cloudomate.hoster.vps.blueangelhost as provider
import cloudomate.gateway.coinbase as Coinbase
from cloudomate import wallet as wallet_util
from cloudomate.hoster.vps.clientarea import ClientArea
from cloudomate.util.settings import Settings
from cloudomate.cmdline import providers as cloudomate_providers
from mock.mock import MagicMock


import plebnet.controllers.cloudomate_controller as cloudomate
import plebnet.agent.dna as DNA
from plebnet.agent.config import PlebNetConfig
from plebnet.utilities import logger as Logger



class TestCloudomateController(unittest.TestCase):

    def test_child_account(self):
        self.cloudomate_settings = Settings.__init__
        self.cloudomate_read = Settings.read_settings
        self.os_is_join = os.path.join
        self.PlebNetConfig = PlebNetConfig.__init__
        self.PlebNetConfig_get = PlebNetConfig.get

        os.path.join = MagicMock()
        Settings.read_settings = MagicMock()
        Settings.__init__ = MagicMock(return_value=None)
        PlebNetConfig.__init__ = MagicMock(return_value=None)
        PlebNetConfig.get = MagicMock(return_value="test")

        # Test child_account with index
        cloudomate.child_account("1")
        os.path.join.assert_called_once()
        Settings.read_settings.assert_called_once()
        Settings.__init__.assert_called_once()
        PlebNetConfig.get.assert_not_called()

        # Test child_account without index
        cloudomate.child_account()
        PlebNetConfig.get.assert_called_once()

        os.path.join = self.os_is_join
        Settings.read_settings = self.cloudomate_read
        Settings.__init__ = self.cloudomate_settings
        PlebNetConfig.__init__ = self.PlebNetConfig
        PlebNetConfig.get = self.PlebNetConfig_get

    def test_vps_providers(self):
        r = cloudomate.get_vps_providers()
        assert len(r) > 0

    def test_status(self):
        self.child_account = cloudomate.child_account
        self.provider = provider.BlueAngelHost.get_status

        cloudomate.child_account = MagicMock()
        provider.BlueAngelHost.get_status = MagicMock()
        assert cloudomate.status(provider.BlueAngelHost)

        cloudomate.child_account = self.child_account
        provider.BlueAngelHost.get_status = self.provider

    def test_get_ip(self):
        self.clientarea = ClientArea.__init__
        self.clientarea_service = ClientArea.get_services
        self.clientarea_ip = ClientArea.get_ip
        self.logger_log = Logger.log

        ClientArea.__init__ = MagicMock(return_value=None)
        Logger.log = MagicMock()
        ClientArea.get_services = MagicMock()
        ClientArea.get_ip = MagicMock()

        cloudomate.get_ip(provider.BlueAngelHost)
        ClientArea.get_ip.assert_called_once()

        ClientArea.__init__ = self.clientarea
        Logger.log = self.logger_log
        ClientArea.get_services = self.clientarea_service
        ClientArea.get_ip = self.clientarea_ip

    def test_options(self):
        self.provider = provider.BlueAngelHost.get_options
        provider.BlueAngelHost.get_options = MagicMock()
        cloudomate.options(provider.BlueAngelHost)
        provider.BlueAngelHost.get_options.assert_called_once()
        provider.BlueAngelHost.get_options = self.provider

    def test_get_network_fee(self):
        self.wallet_util = wallet_util.get_network_fee
        wallet_util.get_network_fee = MagicMock()
        cloudomate.get_network_fee()
        wallet_util.get_network_fee.assert_called_once()
        wallet_util.get_network_fee = self.wallet_util

    def test_pick_providers(self):
        self.DNA = DNA.DNA.choose_provider
        self.vps = cloudomate.get_vps_providers
        self.get_gateway = provider.BlueAngelHost.get_gateway
        self.estimate_price = Coinbase.Coinbase.estimate_price
        self.pick_options = cloudomate.pick_option
        self.get_price = wallet_util.get_price
        self.get_fee = wallet_util.get_network_fee

        DNA.DNA.choose_provider = MagicMock()
        cloudomate.get_vps_providers = MagicMock(return_value=[provider.BlueAngelHost, provider.BlueAngelHost])
        provider.BlueAngelHost.get_gateway = MagicMock()
        Coinbase.Coinbase.estimate_price = MagicMock()
        cloudomate.pick_option = MagicMock(return_value=[1, 2, 3])
        wallet_util.get_price = MagicMock()
        wallet_util.get_network_fee = MagicMock()

        cloudomate.pick_provider(list)
        provider.BlueAngelHost.get_gateway.assert_called_once()

        DNA.DNA.choose_provider = self.DNA
        cloudomate.get_vps_providers = self.vps
        provider.BlueAngelHost.get_gateway = self.get_gateway
        Coinbase.Coinbase.estimate_price = self.estimate_price
        cloudomate.pick_option = self.pick_options
        wallet_util.get_price = self.get_price
        wallet_util.get_network_fee = self.get_fee

    def test_pick_otpions(self):
        self.options = cloudomate.options
        self.providers = cloudomate_providers

        cloudomate.options = MagicMock()
        cloudomate_providers.__init__= MagicMock()
        print cloudomate.pick_option('BlueAngelHost')
        cloudomate.options.assert_called_once()

        cloudomate.options = self.options
        cloudomate_providers.__init__ = self.providers

    #def test_setrootpw(self):
    #    self.clientare = cloudomate.child_account
    #    self.provider = provider
    #    self.put = Settings.put

    #    cloudomate.child_account = MagicMock()
    #    Settings.put = MagicMock()


        #print(cloudomate.child_account())
    #    cloudomate.setrootpw(provider.BlueAngelHost, "Test")


        if __name__ == '__main__':
            unittest.main()

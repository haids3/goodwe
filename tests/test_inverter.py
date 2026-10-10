from unittest import TestCase

from goodwe.inverter import Inverter


class TestDecode(TestCase):

    def test_nul_padded_ascii(self):
        # ESA/EHA-G20 (ARM745) model name register 35011, ASCII padded with NULs
        self.assertEqual("GWGWGW", Inverter._decode(bytes.fromhex("47574757475700000000")))

    def test_space_padded_ascii(self):
        self.assertEqual("GW10K-ET", Inverter._decode(b"GW10K-ET  "))

    def test_utf16(self):
        self.assertEqual("GW10K", Inverter._decode("GW10K".encode("utf-16be")))

    def test_empty(self):
        self.assertEqual("", Inverter._decode(bytes(10)))

from litex.build.generic_platform import *
from litex.build.lattice import LatticePlatform

# IOs ----------------------------------------------------------------------------------------------

_io = [
    ("clk8", 0, Pins("U18"), IOStandard("LVCMOS33")),
    ("programn", 0, Pins("R1"), IOStandard("LVCMOS33")),
    ("serial", 0,
        Subsignal("rx", Pins("U2"), IOStandard("LVCMOS33"), Misc("PULLMODE=UP")),
        Subsignal("tx", Pins("U1"), IOStandard("LVCMOS33")),
    ),
    ("led", 0, Pins("E3 D3 C3 C4 C2 B1 B20 B19 A18 K20 K19"), IOStandard("LVCMOS33")),  # Anodes
    ("led", 1, Pins("P19 L18 K18"), IOStandard("LVCMOS33")), # Cathodes via FET
    ("usb", 0,
        Subsignal("d_p", Pins("F3")),
        Subsignal("d_n", Pins("G3")),
        Subsignal("pullup", Pins("E4")),
        Subsignal("vbusdet", Pins("F4")),
        IOStandard("LVCMOS33")
    ),
    ("keypad", 0,
        Subsignal("left", Pins("G2"), Misc("PULLMODE=UP")),
        Subsignal("right", Pins("F2"), Misc("PULLMODE=UP")),
        Subsignal("up", Pins("F1"), Misc("PULLMODE=UP")),
        Subsignal("down", Pins("C1"), Misc("PULLMODE=UP")),
        Subsignal("start", Pins("E1"), Misc("PULLMODE=UP")),
        Subsignal("select", Pins("D2"), Misc("PULLMODE=UP")),
        Subsignal("a", Pins("D1"), Misc("PULLMODE=UP")),
        Subsignal("b", Pins("E2"), Misc("PULLMODE=UP")),
    ),
    ("hdmi_out", 0,
        Subsignal("clk_p", Pins("P20"), Inverted(), IOStandard("TMDS_33")),
        Subsignal("clk_n", Pins("R20"), Inverted(), IOStandard("TMDS_33")),
        Subsignal("data0_p", Pins("N19"), IOStandard("TMDS_33")),
        Subsignal("data0_n", Pins("N20"), IOStandard("TMDS_33")),
        Subsignal("data1_p", Pins("L20"), IOStandard("TMDS_33")),
        Subsignal("data1_n", Pins("M20"), IOStandard("TMDS_33")),
        Subsignal("data2_p", Pins("L16"), IOStandard("TMDS_33")),
        Subsignal("data2_n", Pins("L17"), IOStandard("TMDS_33")),
        Subsignal("hpd_notif", Pins("R18"), IOStandard("LVCMOS33"), Inverted()),  # Also called HDMI_HEAC_n
        Subsignal("hdmi_heac_p", Pins("T19"), IOStandard("LVCMOS33"), Inverted()),
        Misc("DRIVE=4"),
    ),
    ("lcd", 0,
        Subsignal("db", Pins("J3 H1 K4 J1 K3 K2 L4 K1 L3 L2 M4 L1 M3 M1 N4 N2 N3 N1"), IOStandard("LVCMOS33")),
		Subsignal("rd", Pins("P2"), IOStandard("LVCMOS33")),
		Subsignal("wr", Pins("P4"), IOStandard("LVCMOS33")),
		Subsignal("rs", Pins("P1"), IOStandard("LVCMOS33")),
		Subsignal("cs", Pins("P3"), IOStandard("LVCMOS33")),
		Subsignal("id", Pins("J4"), IOStandard("LVCMOS33")),
		Subsignal("rst", Pins("H2"), IOStandard("LVCMOS33")),
		Subsignal("fmark", Pins("G1"), IOStandard("LVCMOS33")),
		Subsignal("blen", Pins("P5"), IOStandard("LVCMOS33")),
    ),
    ("spiflash", 0, # clock needs to be accessed through USRMCLK
        Subsignal("cs_n", Pins("R2"), IOStandard("LVCMOS33")),
        Subsignal("mosi", Pins("W2"), IOStandard("LVCMOS33")),
        Subsignal("miso", Pins("V2"), IOStandard("LVCMOS33")),
        Subsignal("wp",   Pins("Y2"), IOStandard("LVCMOS33")),
        Subsignal("hold", Pins("W1"), IOStandard("LVCMOS33")),
    ),
    ("spiflash4x", 0, # clock needs to be accessed through USRMCLK
        Subsignal("cs_n", Pins("R2"), IOStandard("LVCMOS33")),
        Subsignal("dq",   Pins("W2 V2 Y2 W1"), IOStandard("LVCMOS33")),
    ),
    ("spiram4x", 0,
        Subsignal("cs_n", Pins("D20"), IOStandard("LVCMOS33"), Misc("SLEWRATE=SLOW")),
        Subsignal("clk",  Pins("E20"), IOStandard("LVCMOS33"), Misc("SLEWRATE=SLOW")),
        Subsignal("dq",   Pins("E19 D19 C20 F19"), IOStandard("LVCMOS33"), Misc("PULLMODE=UP"), Misc("SLEWRATE=SLOW")),
    ),
    ("spiram4x", 1,
        Subsignal("cs_n", Pins("F20"), IOStandard("LVCMOS33"), Misc("SLEWRATE=SLOW")),
        Subsignal("clk",  Pins("J19"), IOStandard("LVCMOS33"), Misc("SLEWRATE=SLOW")),
        Subsignal("dq",   Pins("J20 G19 G20 H20"), IOStandard("LVCMOS33"), Misc("PULLMODE=UP"), Misc("SLEWRATE=SLOW")),
    ),
    ("sao", 0,
        Subsignal("sda", Pins("B3")),
        Subsignal("scl", Pins("B2")),
        Subsignal("gpio", Pins("A2 A3 B4")),
        Subsignal("drm", Pins("A4")),
    ),
    ("sao", 1,
        Subsignal("sda", Pins("A16")),
        Subsignal("scl", Pins("B17")),
        Subsignal("gpio", Pins("B18 A17 B16")),
        Subsignal("drm", Pins("C17")),
    ),
    ("testpts", 0,
        Subsignal("a1", Pins("A15")),
        Subsignal("a2", Pins("C16")),
        Subsignal("a3", Pins("A14")),
        Subsignal("a4", Pins("D16")),
        Subsignal("b1", Pins("B15")),
        Subsignal("b2", Pins("C15")),
        Subsignal("b3", Pins("A13")),
        Subsignal("b4", Pins("B13")),
    ),
#    ("sdram_clock", 0, Pins("22"), IOStandard("LVCMOS33")),
#    ("sdram", 0,
#        Subsignal("a", Pins("17 18 19 20 30 29 28 27 26 25 16 24 09")),
#        Subsignal("dq", Pins("01 03 05 07 02 04 06 08")),
#        Subsignal("we_n", Pins("10")),
#        Subsignal("ras_n", Pins("12")),
#        Subsignal("cas_n", Pins("11")),
#        Subsignal("cs_n", Pins("13")),
#        Subsignal("cke", Pins("23")),
#        Subsignal("ba", Pins("14 15")),
#        Subsignal("dm", Pins("21")),
#        IOStandard("LVCMOS33"), Misc("SLEWRATE=FAST")
#    ),
    ("sdram_clock", 0, Pins("C11"), IOStandard("LVCMOS33")),
    ("sdram", 0,
        Subsignal("a", Pins("D10 C10 B10 A10 C14 E17 A12 B12 H17 G18 A9 A11 A7")),
        Subsignal("dq", Pins("C5 A5 B6 D6 B5 C6 A6 C7")),
        Subsignal("we_n", Pins("C8")),
        Subsignal("ras_n", Pins("A8")),
        Subsignal("cas_n", Pins("B8")),
        Subsignal("cs_n", Pins("D9")),
        Subsignal("cke", Pins("B11")),
        Subsignal("ba", Pins("C9 B9")),
        Subsignal("dm", Pins("D11")),
        IOStandard("LVCMOS33"), Misc("SLEWRATE=FAST")
    ),
    #("C5 B5 A5 C6 B6 A6 D6 C7 A7 C8 B8 A8 D9 C9 B9 A9 D10 C10 B10 A10 D11 C11 B11 A11 G18 H17 B12 A12 E17 C14"),
    #("01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17  18  19  20  21  22  23  24  25  26  27  28  29  30 "),

    # Only used for simulation
    ("wishbone", 0,
        Subsignal("adr",   Pins(30)),
        Subsignal("dat_r", Pins(32)),
        Subsignal("dat_w", Pins(32)),
        Subsignal("sel",   Pins(4)),
        Subsignal("cyc",   Pins(1)),
        Subsignal("stb",   Pins(1)),
        Subsignal("ack",   Pins(1)),
        Subsignal("we",    Pins(1)),
        Subsignal("cti",   Pins(3)),
        Subsignal("bte",   Pins(2)),
        Subsignal("err",   Pins(1))
    ),
    ("reset", 0, Pins(1), IOStandard("LVCMOS33")),
]

_connectors = [
    ("pmod", "A15 C16 A14 D16 B15 C15 A13 B13"),
    ("genio", "C5 B5 A5 C6 B6 A6 D6 C7 A7 C8 B8 A8 D9 C9 B9 A9 D10 C10 B10 A10 D11 C11 B11 A11 G18 H17 B12 A12 E17 C14"),
]

_pmod_gpio = [
    ("pmod_gpio", 0,
     Subsignal("p0", Pins("pmod:0")),
     Subsignal("p1", Pins("pmod:1")),
     Subsignal("p2", Pins("pmod:2")),
     Subsignal("p3", Pins("pmod:3")),
     Subsignal("p4", Pins("pmod:4")),
     Subsignal("p5", Pins("pmod:5")),
     Subsignal("p6", Pins("pmod:6")),
     Subsignal("p7", Pins("pmod:7")),
     IOStandard("LVCMOS33")
    ),
]

_genio_gpio = [
    ("genio_gpio", 0,
     Subsignal("p0", Pins("genio:0")),
     Subsignal("p1", Pins("genio:1")),
     Subsignal("p2", Pins("genio:2")),
     Subsignal("p3", Pins("genio:3")),
     Subsignal("p4", Pins("genio:4")),
     Subsignal("p5", Pins("genio:5")),
     Subsignal("p6", Pins("genio:6")),
     Subsignal("p7", Pins("genio:7")),
     Subsignal("p8", Pins("genio:8")),
     Subsignal("p9", Pins("genio:9")),

     Subsignal("p10", Pins("genio:10")),
     Subsignal("p11", Pins("genio:11")),
     Subsignal("p12", Pins("genio:12")),
     Subsignal("p13", Pins("genio:13")),
     Subsignal("p14", Pins("genio:14")),
     Subsignal("p15", Pins("genio:15")),
     Subsignal("p16", Pins("genio:16")),
     Subsignal("p17", Pins("genio:17")),
     Subsignal("p18", Pins("genio:18")),
     Subsignal("p19", Pins("genio:19")),

     Subsignal("p20", Pins("genio:20")),
     Subsignal("p21", Pins("genio:21")),
     Subsignal("p22", Pins("genio:22")),
     Subsignal("p23", Pins("genio:23")),
     Subsignal("p24", Pins("genio:24")),
     Subsignal("p25", Pins("genio:25")),
     Subsignal("p26", Pins("genio:26")),
     Subsignal("p27", Pins("genio:27")),
     Subsignal("p28", Pins("genio:28")),
     Subsignal("p29", Pins("genio:29")),
    )
]

# Platform -----------------------------------------------------------------------------------------

class Platform(LatticePlatform):
    default_clk_name = "clk8"
    default_clk_period = 1e9/8e6

    def __init__(self, device="LFE5U-45F", **kwargs):
        LatticePlatform.__init__(self, device + "-CABGA381", io=_io, connectors=_connectors, toolchain="trellis", **kwargs)

    def create_programmer(self):
        raise ValueError("{} programmer is not supported"
                             .format(self.programmer))

    def do_finalize(self, fragment):
        LatticePlatform.do_finalize(self, fragment)

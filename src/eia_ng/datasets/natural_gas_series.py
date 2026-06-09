from typing import Dict

WEEKLY_WORKING_STORAGE_SERIES_BY_REGION: Dict[str, str] = {
    "lower48": "NW2_EPG0_SWO_R48_BCF",
    "east": "NW2_EPG0_SWO_R31_BCF",
    "midwest": "NW2_EPG0_SWO_R32_BCF",
    "south_central": "NW2_EPG0_SWO_R33_BCF",
    "mountain": "NW2_EPG0_SWO_R34_BCF",
    "pacific": "NW2_EPG0_SWO_R35_BCF",
    # South Central breakdown
    "south_central_nonsalt": "NW2_EPG0_SNO_R33_BCF",
    "south_central_salt": "NW2_EPG0_SSO_R33_BCF",
}

# Base Gas
BASE_GAS_STORAGE_SERIES_BY_GEOGRAPHY = {
    "al": "N5010AL2",
    "ar": "N5010AR2",
    "ca": "N5010CA2",
    "co": "N5010CO2",
    "ia": "N5010IA2",
    "il": "N5010IL2",
    "in": "N5010IN2",
    "ks": "N5010KS2",
    "ky": "N5010KY2",
    "la": "N5010LA2",
    "md": "N5010MD2",
    "mi": "N5010MI2",
    "mn": "N5010MN2",
    "mo": "N5010MO2",
    "ms": "N5010MS2",
    "mt": "N5010MT2",
    "ne": "N5010NE2",
    "nm": "N5010NM2",
    "ny": "N5010NY2",
    "oh": "N5010OH2",
    "ok": "N5010OK2",
    "or": "N5010OR2",
    "pa": "N5010PA2",
    "tn": "N5010TN2",
    "tx": "N5010TX2",
    "ut": "N5010UT2",
    "va": "N5010VA2",
    "wa": "N5010WA2",
    "wv": "N5010WV2",
    "wy": "N5010WY2",
    "east": "N5010832",
    "south_central": "N5010842",
    "midwest": "N5010852",
    "mountain": "N5010862",
    "aga_producing": "N5010872",
    "aga_eastern_consuming": "N5010882",
    "aga_western_consuming": "N5010892",
    "pacific": "N5010912",
    "us_total": "N5010US2",
}


# WORKING GAS
UNDERGROUND_STORAGE_WORKING_GAS_SERIES_BY_GEOGRAPHY = {
    "al": "N5020AL2",
    "ar": "N5020AR2",
    "ca": "N5020CA2",
    "co": "N5020CO2",
    "ia": "N5020IA2",
    "il": "N5020IL2",
    "in": "N5020IN2",
    "ks": "N5020KS2",
    "ky": "N5020KY2",
    "la": "N5020LA2",
    "md": "N5020MD2",
    "mi": "N5020MI2",
    "mn": "N5020MN2",
    "mo": "N5020MO2",
    "ms": "N5020MS2",
    "mt": "N5020MT2",
    "ne": "N5020NE2",
    "nm": "N5020NM2",
    "ny": "N5020NY2",
    "oh": "N5020OH2",
    "ok": "N5020OK2",
    "or": "N5020OR2",
    "pa": "N5020PA2",
    "tn": "N5020TN2",
    "tx": "N5020TX2",
    "ut": "N5020UT2",
    "va": "N5020VA2",
    "wa": "N5020WA2",
    "wv": "N5020WV2",
    "wy": "N5020WY2",
    "east": "N5020832",
    "south_central": "N5020842",
    "midwest": "N5020852",
    "mountain": "N5020862",
    "aga_producing": "N5020872",
    "aga_eastern_consuming": "N5020882",
    "aga_western_consuming": "N5020892",
    "pacific": "N5020912",
    "us_total": "N5020US2",
}

# Total Gas
UNDERGROUND_STORAGE_TOTAL_GAS_SERIES_BY_GEOGRAPHY = {
    "al": "N5030AL2",
    "ar": "N5030AR2",
    "ca": "N5030CA2",
    "co": "N5030CO2",
    "ia": "N5030IA2",
    "il": "N5030IL2",
    "in": "N5030IN2",
    "ks": "N5030KS2",
    "ky": "N5030KY2",
    "la": "N5030LA2",
    "md": "N5030MD2",
    "mi": "N5030MI2",
    "mn": "N5030MN2",
    "mo": "N5030MO2",
    "ms": "N5030MS2",
    "mt": "N5030MT2",
    "ne": "N5030NE2",
    "nm": "N5030NM2",
    "ny": "N5030NY2",
    "oh": "N5030OH2",
    "ok": "N5030OK2",
    "or": "N5030OR2",
    "pa": "N5030PA2",
    "tn": "N5030TN2",
    "tx": "N5030TX2",
    "ut": "N5030UT2",
    "va": "N5030VA2",
    "wa": "N5030WA2",
    "wv": "N5030WV2",
    "wy": "N5030WY2",
    "east": "N5030832",
    "south_central": "N5030842",
    "midwest": "N5030852",
    "mountain": "N5030862",
    "aga_producing": "N5030872",
    "aga_eastern_consuming": "N5030882",
    "aga_western_consuming": "N5030892",
    "pacific": "N5030912",
    "us_total": "N5030US2",
}

# working gas yoy volume
UNDERGROUND_STORAGE_WORKING_GAS_YOY_VOLUME_SERIES_BY_GEOGRAPHY = {
    "al": "N5040AL2",
    "ar": "N5040AR2",
    "ca": "N5040CA2",
    "co": "N5040CO2",
    "ia": "N5040IA2",
    "il": "N5040IL2",
    "in": "N5040IN2",
    "ks": "N5040KS2",
    "ky": "N5040KY2",
    "la": "N5040LA2",
    "md": "N5040MD2",
    "mi": "N5040MI2",
    "mn": "N5040MN2",
    "mo": "N5040MO2",
    "ms": "N5040MS2",
    "mt": "N5040MT2",
    "ne": "N5040NE2",
    "nm": "N5040NM2",
    "ny": "N5040NY2",
    "oh": "N5040OH2",
    "ok": "N5040OK2",
    "or": "N5040OR2",
    "pa": "N5040PA2",
    "tn": "N5040TN2",
    "tx": "N5040TX2",
    "ut": "N5040UT2",
    "va": "N5040VA2",
    "wa": "N5040WA2",
    "wv": "N5040WV2",
    "wy": "N5040WY2",
    "east": "N5040832",
    "south_central": "N5040842",
    "midwest": "N5040852",
    "mountain": "N5040862",
    "aga_producing": "N5040872",
    "aga_eastern_consuming": "N5040882",
    "aga_western_consuming": "N5040892",
    "pacific": "N5040912",
    "us_total": "N5040US2",
}


# working gas yoy percent
UNDERGROUND_STORAGE_WORKING_GAS_YOY_PERCENT_SERIES_BY_GEOGRAPHY = {
    "al": "N5040AL4",
    "ar": "N5040AR4",
    "ca": "N5040CA4",
    "co": "N5040CO4",
    "ia": "N5040IA4",
    "il": "N5040IL4",
    "in": "N5040IN4",
    "ks": "N5040KS4",
    "ky": "N5040KY4",
    "la": "N5040LA4",
    "md": "N5040MD4",
    "mi": "N5040MI4",
    "mn": "N5040MN4",
    "mo": "N5040MO4",
    "ms": "N5040MS4",
    "mt": "N5040MT4",
    "ne": "N5040NE4",
    "nm": "N5040NM4",
    "ny": "N5040NY4",
    "oh": "N5040OH4",
    "ok": "N5040OK4",
    "or": "N5040OR4",
    "pa": "N5040PA4",
    "tn": "N5040TN4",
    "tx": "N5040TX4",
    "ut": "N5040UT4",
    "va": "N5040VA4",
    "wa": "N5040WA4",
    "wv": "N5040WV4",
    "wy": "N5040WY4",
    "east": "N5040834",
    "south_central": "N5040844",
    "midwest": "N5040854",
    "mountain": "N5040864",
    "aga_producing": "N5040874",
    "aga_eastern_consuming": "N5040884",
    "aga_western_consuming": "N5040894",
    "pacific": "N5040914",
    "us_total": "N5040US4",
}


# underground injections
UNDERGROUND_STORAGE_INJECTIONS_SERIES_BY_GEOGRAPHY = {
    "al": "N5050AL2",
    "ar": "N5050AR2",
    "ca": "N5050CA2",
    "co": "N5050CO2",
    "ia": "N5050IA2",
    "il": "N5050IL2",
    "in": "N5050IN2",
    "ks": "N5050KS2",
    "ky": "N5050KY2",
    "la": "N5050LA2",
    "md": "N5050MD2",
    "mi": "N5050MI2",
    "mn": "N5050MN2",
    "mo": "N5050MO2",
    "ms": "N5050MS2",
    "mt": "N5050MT2",
    "ne": "N5050NE2",
    "nm": "N5050NM2",
    "ny": "N5050NY2",
    "oh": "N5050OH2",
    "ok": "N5050OK2",
    "or": "N5050OR2",
    "pa": "N5050PA2",
    "tn": "N5050TN2",
    "tx": "N5050TX2",
    "ut": "N5050UT2",
    "va": "N5050VA2",
    "wa": "N5050WA2",
    "wv": "N5050WV2",
    "wy": "N5050WY2",
    "east": "N5050832",
    "south_central": "N5050842",
    "midwest": "N5050852",
    "mountain": "N5050862",
    "aga_producing": "N5050872",
    "aga_eastern_consuming": "N5050882",
    "aga_western_consuming": "N5050892",
    "pacific": "N5050912",
    "us_total": "N5050US2",
}


# withdrawls
UNDERGROUND_STORAGE_WITHDRAWALS_SERIES_BY_GEOGRAPHY = {
    "al": "N5060AL2",
    "ar": "N5060AR2",
    "ca": "N5060CA2",
    "co": "N5060CO2",
    "ia": "N5060IA2",
    "il": "N5060IL2",
    "in": "N5060IN2",
    "ks": "N5060KS2",
    "ky": "N5060KY2",
    "la": "N5060LA2",
    "md": "N5060MD2",
    "mi": "N5060MI2",
    "mn": "N5060MN2",
    "mo": "N5060MO2",
    "ms": "N5060MS2",
    "mt": "N5060MT2",
    "ne": "N5060NE2",
    "nm": "N5060NM2",
    "ny": "N5060NY2",
    "oh": "N5060OH2",
    "ok": "N5060OK2",
    "or": "N5060OR2",
    "pa": "N5060PA2",
    "tn": "N5060TN2",
    "tx": "N5060TX2",
    "ut": "N5060UT2",
    "va": "N5060VA2",
    "wa": "N5060WA2",
    "wv": "N5060WV2",
    "wy": "N5060WY2",
    "east": "N5060832",
    "south_central": "N5060842",
    "midwest": "N5060852",
    "mountain": "N5060862",
    "aga_producing": "N5060872",
    "aga_eastern_consuming": "N5060882",
    "aga_western_consuming": "N5060892",
    "pacific": "N5060912",
    "us_total": "N5060US2",
}

# net withdrawls
UNDERGROUND_STORAGE_NET_WITHDRAWALS_SERIES_BY_GEOGRAPHY = {
    "al": "N5070AL2",
    "ar": "N5070AR2",
    "ca": "N5070CA2",
    "co": "N5070CO2",
    "ia": "N5070IA2",
    "il": "N5070IL2",
    "in": "N5070IN2",
    "ks": "N5070KS2",
    "ky": "N5070KY2",
    "la": "N5070LA2",
    "md": "N5070MD2",
    "mi": "N5070MI2",
    "mn": "N5070MN2",
    "mo": "N5070MO2",
    "ms": "N5070MS2",
    "mt": "N5070MT2",
    "ne": "N5070NE2",
    "nm": "N5070NM2",
    "ny": "N5070NY2",
    "oh": "N5070OH2",
    "ok": "N5070OK2",
    "or": "N5070OR2",
    "pa": "N5070PA2",
    "tn": "N5070TN2",
    "tx": "N5070TX2",
    "ut": "N5070UT2",
    "va": "N5070VA2",
    "wa": "N5070WA2",
    "wv": "N5070WV2",
    "wy": "N5070WY2",
    "east": "N5070832",
    "south_central": "N5070842",
    "midwest": "N5070852",
    "mountain": "N5070862",
    "aga_producing": "N5070872",
    "aga_eastern_consuming": "N5070882",
    "aga_western_consuming": "N5070892",
    "pacific": "N5070912",
    "us_total": "N5070US2",
}

UNDERGROUND_STORAGE_TYPE = {
    "base_gas": "N5010US2",
    "working_gas": "N5020US2",
    "total_gas": "N5030US2",
    "injections": "N5050US2",
    "withdrawals": "N5060US2",
    "net_withdrawals": "N5070US2",
    "salt_base_gas": "N5400US2",
    "salt_working_gas": "N5410US2",
    "salt_total_gas": "N5420US2",
    "salt_injections": "N5440US2",
    "salt_withdrawals": "N5450US2",
    "salt_net_withdrawals": "N5460US2",
    "nonsalt_base_gas": "N5500US2",
    "nonsalt_working_gas": "N5510US2",
    "nonsalt_total_gas": "N5520US2",
    "nonsalt_injections": "N5540US2",
    "nonsalt_withdrawals": "N5550US2",
    "nonsalt_net_withdrawals": "N5560US2",
}

PRODUCTION_SERIES_BY_STATE = {
    "al": "NA1160_SAL_2",
    "ak": "NA1160_SAK_2",
    "az": "NA1160_SAZ_2",
    "ar": "NA1160_SAR_2",
    "ca": "NA1160_SCA_2",
    "co": "NA1160_SCO_2",
    "fl": "NA1160_SFL_2",
    "il": "NA1160_SIL_2",
    "in": "NA1160_SIN_2",
    "ks": "NA1160_SKS_2",
    "ky": "NA1160_SKY_2",
    "la": "NA1160_SLA_2",
    "md": "NA1160_SMD_2",
    "mi": "NA1160_SMI_2",
    "mo": "NA1160_SMO_2",
    "ms": "NA1160_SMS_2",
    "mt": "NA1160_SMT_2",
    "ne": "NA1160_SNE_2",
    "nv": "NA1160_SNV_2",
    "nm": "NA1160_SNM_2",
    "ny": "NA1160_SNY_2",
    "nd": "NA1160_SND_2",
    "oh": "NA1160_SOH_2",
    "ok": "NA1160_SOK_2",
    "or": "NA1160_SOR_2",
    "pa": "NA1160_SPA_2",
    "sd": "NA1160_SSD_2",
    "tn": "NA1160_STN_2",
    "tx": "NA1160_STX_2",
    "ut": "NA1160_SUT_2",
    "va": "NA1160_SVA_2",
    "wv": "NA1160_SWV_2",
    "united_states_total": "N9070US2",
}


CONSUMPTION_SERIES_BY_STATE = {
    "al": "N9140AL2",
    "ak": "N9140AK2",
    "az": "N9140AZ2",
    "ar": "N9140AR2",
    "ca": "N9140CA2",
    "co": "N9140CO2",
    "ct": "N9140CT2",
    "de": "N9140DE2",
    "fl": "N9140FL2",
    "ga": "N9140GA2",
    "hi": "N9140HI2",
    "id": "N9140ID2",
    "il": "N9140IL2",
    "in": "N9140IN2",
    "ia": "N9140IA2",
    "ks": "N9140KS2",
    "ky": "N9140KY2",
    "la": "N9140LA2",
    "me": "N9140ME2",
    "md": "N9140MD2",
    "ma": "N9140MA2",
    "mi": "N9140MI2",
    "mn": "N9140MN2",
    "ms": "N9140MS2",
    "mo": "N9140MO2",
    "mt": "N9140MT2",
    "ne": "N9140NE2",
    "nv": "N9140NV2",
    "nh": "N9140NH2",
    "nj": "N9140NJ2",
    "nm": "N9140NM2",
    "ny": "N9140NY2",
    "nc": "N9140NC2",
    "nd": "N9140ND2",
    "oh": "N9140OH2",
    "ok": "N9140OK2",
    "or": "N9140OR2",
    "pa": "N9140PA2",
    "ri": "N9140RI2",
    "sc": "N9140SC2",
    "sd": "N9140SD2",
    "tn": "N9140TN2",
    "tx": "N9140TX2",
    "ut": "N9140UT2",
    "vt": "N9140VT2",
    "va": "N9140VA2",
    "wa": "N9140WA2",
    "wv": "N9140WV2",
    "wi": "N9140WI2",
    "wy": "N9140WY2",
    "united_states_total": "N9140US2",
}

IMPORT_SERIES_BY_COUNTRY = {
    # pipeline imports
    "canada_pipeline": "N9102CN2",
    "mexico_pipeline": "N9102MX2",
    "united_states_pipeline_total": "N9102US2",
    # LNG imports by country
    "algeria": "N9103AG2",
    "australia": "N9103AU2",
    "brunei": "N9103BX2",
    "egypt": "N9103EG2",
    "equatorial_guinea": "NGM_EPG0_NUS-NEK_IML_MMCF",
    "france": "NGM_EPG0_IML_NUS-NFR_MMCF",
    "indonesia": "N9103ID2",
    "jamaica": "NGM_EPG0_IML_NUS-NJM_MMCF",
    "malaysia": "N9103MY2",
    "nigeria": "N9103NG2",
    "norway": "NGM_EPG0_NUS-NNO_IML_MMCF",
    "oman": "N9103MU2",
    "peru": "NGM_EPG0_NUS-NPE_IML_MMCF",
    "qatar": "N9103QR2",
    "trinidad_and_tobago": "N9103TD2",
    "united_arab_emirates": "N9103UA2",
    "united_kingdom": "NGM_EPG0_IML_NUS-NUK_MMCF",
    "yemen": "NGM_EPG0_IML_NUS-NYE_MMCF",
    # LNG aggregate
    "united_states_lng_total": "N9103US2",
    # compressed natural gas
    "canada_compressed": "NGM_EPG0_INC_NUS-NCA_MMCF",
    "united_states_compressed_total": "NGM_EPG0_INC_NUS-Z00_MMCF",
}

EXPORT_SERIES_BY_COUNTRY = {
    # pipeline exports
    "canada_pipeline": "N9132CN2",
    "mexico_pipeline": "N9132MX2",
    "united_states_pipeline_total": "N9132US2",
    # LNG exports by vessel
    "argentina": "NGM_EPG0_EVE_NUS-NAT_MMCF",
    "australia": "NGM_EPG0_EVE_NUS-NAU_MMCF",
    "bahrain": "NGM_EPG0_EVE_NUS-NBA_MMCF",
    "bangladesh": "NGM_EPG0_EVE_NUS-NBG_MMCF",
    "barbados": "NGM_EPG0_EVE_NUS-NBB_MMCF",
    "belgium": "NGM_EPG0_EVE_NUS-NBE_MMCF",
    "brazil": "NGM_EPG0_EVE_NUS-NBR_MMCF",
    "chile": "NGM_EPG0_EVE_NUS-NCI_MMCF",
    "china": "NGM_EPG0_EVE_NUS-NCH_MMCF",
    "colombia": "NGM_EPG0_EVE_NUS-NCO_MMCF",
    "croatia": "NGM_EPG0_EVE_NUS-NHR_MMCF",
    "dominican_republic": "NGM_EPG0_EVE_NUS-NDR_MMCF",
    "egypt": "NGM_EPG0_EVE_NUS-NEG_MMCF",
    "el_salvador": "NGM_EPG0_EVE_NUS-NES_MMCF",
    "finland": "NGM_EPG0_EVE_NUS-NFL_MMCF",
    "france": "NGM_EPG0_EVE_NUS-NFR_MMCF",
    "germany": "NGM_EPG0_EVE_NUS-NGM_MMCF",
    "greece": "NGM_EPG0_EVE_NUS-NGR_MMCF",
    "haiti": "NGM_EPG0_EVE_NUS-NHA_MMCF",
    "india": "NGM_EPG0_EVE_NUS-NIN_MMCF",
    "indonesia": "NGM_EPG0_EVE_NUS-NID_MMCF",
    "israel": "NGM_EPG0_EVE_NUS-NIS_MMCF",
    "italy": "NGM_EPG0_EVE_NUS-NIT_MMCF",
    "jamaica": "NGM_EPG0_EVE_NUS-NJM_MMCF",
    "japan": "NGM_EPG0_EVE_NUS-NJA_MMCF",
    "jordan": "NGM_EPG0_EVE_NUS-NJO_MMCF",
    "kuwait": "NGM_EPG0_EVE_NUS-NKU_MMCF",
    "lithuania": "NGM_EPG0_EVE_NUS-NLH_MMCF",
    "malta": "NGM_EPG0_EVE_NUS-NM6_MMCF",
    "mauritania": "NGM_EPG0_EVE_NUS-NMR_MMCF",
    "mexico": "NGM_EPG0_EVE_NUS-NMX_MMCF",
    "netherlands": "NGM_EPG0_EVE_NUS-NNL_MMCF",
    "nicaragua": "NGM_EPG0_EVE_NUS-NNU_MMCF",
    "pakistan": "NGM_EPG0_EVE_NUS-NPK_MMCF",
    "panama": "NGM_EPG0_EVE_NUS-NPM_MMCF",
    "philippines": "NGM_EPG0_EVE_NUS-NRP_MMCF",
    "poland": "NGM_EPG0_EVE_NUS-NPL_MMCF",
    "portugal": "NGM_EPG0_EVE_NUS-NPO_MMCF",
    "russia": "NGM_EPG0_EVE_NUS-NRS_MMCF",
    "senegal": "NGM_EPG0_EVE_NUS-NSG_MMCF",
    "singapore": "NGM_EPG0_EVE_NUS-NSN_MMCF",
    "south_korea": "NGM_EPG0_EVE_NUS-NKS_MMCF",
    "spain": "NGM_EPG0_EVE_NUS-NSP_MMCF",
    "taiwan": "NGM_EPG0_EVE_NUS-NTW_MMCF",
    "thailand": "NGM_EPG0_EVE_NUS-NTH_MMCF",
    "turkiye": "NGM_EPG0_EVE_NUS-NTU_MMCF",
    "united_arab_emirates": "NGM_EPG0_EVE_NUS-NTC_MMCF",
    "united_kingdom": "NGM_EPG0_EVE_NUS-NUK_MMCF",
    # LNG aggregate
    "united_states_lng_total": "N9133US2",
    # truck exports
    "canada_truck": "NGM_EPG0_ETR_NUS-NCA_MMCF",
    "mexico_truck": "NGM_EPG0_ETR_NUS-NMX_MMCF",
    "united_states_truck_total": "NGM_EPG0_ETR_NUS-Z00_MMCF",
    # compressed natural gas exports
    "canada_compressed": "NGM_EPG0_ENC_NUS-NCA_MMCF",
    "united_states_compressed_total": "NGM_EPG0_ENC_NUS-Z00_MMCF",
}

FUTURES_SERIES_BY_CONTRACT = {
    1: "RNGC1",
    2: "RNGC2",
    3: "RNGC3",
    4: "RNGC4",
}


# ===============================
# Natural Gas – Proved Reserves
# Wet, After Lease Separation
# Associated-Dissolved (BCF)
# ===============================

NG_PROVED_WET_ASSOC_BY_STATE = {
    "al": "RNGR41SAL_1",  # Alabama
    "ak": "RNGR41SAK_1",  # Alaska
    "ar": "RNGR41SAR_1",  # Arkansas
    "ca": "RNGR41SCA_1",  # California
    "co": "RNGR41SCO_1",  # Colorado
    "fl": "RNGR41SFL_1",  # Florida
    "ks": "RNGR41SKS_1",  # Kansas
    "ky": "RNGR41SKY_1",  # Kentucky
    "la": "RNGR41SLA_1",  # Louisiana
    "mi": "RNGR41SMI_1",  # Michigan
    "ms": "RNGR41SMS_1",  # Mississippi
    "mt": "RNGR41SMT_1",  # Montana
    "nd": "RNGR41SND_1",  # North Dakota
    "nm": "RNGR41SNM_1",  # New Mexico
    "ny": "RNGR41SNY_1",  # New York
    "oh": "RNGR41SOH_1",  # Ohio
    "ok": "RNGR41SOK_1",  # Oklahoma
    "pa": "RNGR41SPA_1",  # Pennsylvania
    "tx": "RNGR41STX_1",  # Texas
    "ut": "RNGR41SUT_1",  # Utah
    "va": "RNGR41SVA_1",  # Virginia
    "wv": "RNGR41SWV_1",  # West Virginia
    "wy": "RNGR41SWY_1",  # Wyoming
    # U.S. total
    "us": "RNGR41NUS_1",
    "all": "RNGR41NUS_1",
}

# ===============================
# Natural Gas – Proved Reserves
# Wet, After Lease Separation
# Nonassociated (BCF)
# ===============================

NG_PROVED_WET_NONASSOC_BY_STATE = {
    "al": "RNGR31SAL_1",  # Alabama
    "ak": "RNGR31SAK_1",  # Alaska
    "ar": "RNGR31SAR_1",  # Arkansas
    "ca": "RNGR31SCA_1",  # California
    "co": "RNGR31SCO_1",  # Colorado
    "fl": "RNGR31SFL_1",  # Florida
    "ks": "RNGR31SKS_1",  # Kansas
    "ky": "RNGR31SKY_1",  # Kentucky
    "la": "RNGR31SLA_1",  # Louisiana
    "mi": "RNGR31SMI_1",  # Michigan
    "ms": "RNGR31SMS_1",  # Mississippi
    "mt": "RNGR31SMT_1",  # Montana
    "nd": "RNGR31SND_1",  # North Dakota
    "nm": "RNGR31SNM_1",  # New Mexico
    "ny": "RNGR31SNY_1",  # New York
    "oh": "RNGR31SOH_1",  # Ohio
    "ok": "RNGR31SOK_1",  # Oklahoma
    "pa": "RNGR31SPA_1",  # Pennsylvania
    "tx": "RNGR31STX_1",  # Texas
    "ut": "RNGR31SUT_1",  # Utah
    "va": "RNGR31SVA_1",  # Virginia
    "wv": "RNGR31SWV_1",  # West Virginia
    "wy": "RNGR31SWY_1",  # Wyoming
    # U.S. total
    "us": "RNGR31NUS_1",
    "all": "RNGR31NUS_1",
}

# ===============================
# Natural Gas Plant Liquids
# Proved Reserves (MMBbl)
# ===============================

NGL_PROVED_BY_STATE = {
    "al": "RL2R01SAL_1",  # Alabama
    "ak": "RL2R01SAK_1",  # Alaska
    "ar": "RL2R01SAR_1",  # Arkansas
    "ca": "RL2R01SCA_1",  # California
    "co": "RL2R01SCO_1",  # Colorado
    "fl": "RL2R01SFL_1",  # Florida
    "ks": "RL2R01SKS_1",  # Kansas
    "ky": "RL2R01SKY_1",  # Kentucky
    "la": "RL2R01SLA_1",  # Louisiana
    "mi": "RL2R01SMI_1",  # Michigan
    "ms": "RL2R01SMS_1",  # Mississippi
    "mt": "RL2R01SMT_1",  # Montana
    "nd": "RL2R01SND_1",  # North Dakota
    "nm": "RL2R01SNM_1",  # New Mexico
    "ny": "RL2R01SNY_1",  # New York
    "oh": "RL2R01SOH_1",  # Ohio
    "ok": "RL2R01SOK_1",  # Oklahoma
    "pa": "RL2R01SPA_1",  # Pennsylvania
    "tx": "RL2R01STX_1",  # Texas
    "ut": "RL2R01SUT_1",  # Utah
    "va": "RL2R01SVA_1",  # Virginia
    "wv": "RL2R01SWV_1",  # West Virginia
    "wy": "RL2R01SWY_1",  # Wyoming
    # U.S. total
    "us": "RL2R01NUS_1",
    "all": "RL2R01NUS_1",
}


# ===============================
# Natural Gas – Expected Future Production
# Dry Natural Gas (BCF)
# ===============================

NG_EFP_DRY_BY_STATE = {
    "al": "RNGR11SAL_1",  # Alabama
    "ak": "RNGR11SAK_1",  # Alaska
    "ar": "RNGR11SAR_1",  # Arkansas
    "ca": "RNGR11SCA_1",  # California
    "co": "RNGR11SCO_1",  # Colorado
    "fl": "RNGR11SFL_1",  # Florida
    "ks": "RNGR11SKS_1",  # Kansas
    "ky": "RNGR11SKY_1",  # Kentucky
    "la": "RNGR11SLA_1",  # Louisiana
    "mi": "RNGR11SMI_1",  # Michigan
    "ms": "RNGR11SMS_1",  # Mississippi
    "mt": "RNGR11SMT_1",  # Montana
    "nd": "RNGR11SND_1",  # North Dakota
    "nm": "RNGR11SNM_1",  # New Mexico
    "ny": "RNGR11SNY_1",  # New York
    "oh": "RNGR11SOH_1",  # Ohio
    "ok": "RNGR11SOK_1",  # Oklahoma
    "pa": "RNGR11SPA_1",  # Pennsylvania
    "tx": "RNGR11STX_1",  # Texas
    "ut": "RNGR11SUT_1",  # Utah
    "va": "RNGR11SVA_1",  # Virginia
    "wv": "RNGR11SWV_1",  # West Virginia
    "wy": "RNGR11SWY_1",  # Wyoming
    # U.S. total
    "us": "RNGR11NUS_1",
    "all": "RNGR11NUS_1",
}

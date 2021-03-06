set RESULT_DIR "./output"
set alta_work "${RESULT_DIR}/alta_db"

set DEVICE "AG10KSDE176"
set TOP_MODULE "Blinky"
set verilog "Blinky.vqm"
set sdc "Blinky.sdc"

# alta::set_debug_cmd ar_bitgen 1
# alta::set_debug_cmd ar_chain_config 1
# alta::set_debug_cmd ar_io 1
# alta::set_debug_cmd ar_bbtile 1
# alta::set_debug_cmd ar_slice_ram 1
# alta::set_debug_cmd ar_toptile 1

load_architect -type ${DEVICE} 1 1 1000 1000

read_design_and_pack -top ${TOP_MODULE} $verilog
read_sdc $sdc

place_and_route_design

write_routed_design "${RESULT_DIR}/${TOP_MODULE}_routed.v" 
alta::dump_route_list_cmd 1

bitgen normal -prg "${RESULT_DIR}/${TOP_MODULE}.prg" -bin "${RESULT_DIR}/${TOP_MODULE}.bin"


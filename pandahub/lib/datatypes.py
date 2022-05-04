
datatypes = {
    "bus": {
        "name": str,
        "vn_kv": float,
        "type": str,
        "zone": str,
        "in_service": bool,
        "max_vm_pu": float,
        "min_vm_pu": float
    },
    "load": {
        "name": str,
        "bus": int,
        "p_mw": float,
        "q_mvar": float,
        "const_z_percent": float,
        "const_i_percent": float,
        "sn_mva": float,
        "scaling": float,
        "in_service": bool,
        "controllable": bool,
        "type": str
    },
    "sgen": {
        "name": str,
        "bus": int,
        "p_mw": float,
        "q_mvar": float,
        "sn_mva": float,
        "scaling": float,
        "in_service": bool,
        "type": str,
        "current_source": bool
    },
    "gen": {
        "name": str,
        "bus": int,
        "p_mw": float,
        "vm_pu": float,
        "sn_mva": float,
        "min_q_mvar": float,
        "max_q_mvar": float,
        "scaling": float,
        "slack": bool,
        "in_service": bool,
        "type": str,
        "slack_weight": float,
        "controllable": bool,
        "max_p_mw": float,
        "min_p_mw": float
    },
    "switch": {
        "name": str,
        "bus": int,
        "element": int,
        "et": str,
        "type": str,
        "closed": bool,
        "z_ohm": float
    },
    "ext_grid": {
        "name": str,
        "bus": int,
        "vm_pu": float,
        "va_degree": float,
        "slack_weight": float,
        "in_service": bool,
        "max_p_mw": float,
        "min_p_mw": float,
        "max_q_mvar": float,
        "min_q_mvar": float
    },
    "line": {
        "name": str,
        "from_bus": int,
        "to_bus": int,
        "length_km": float,
        "r_ohm_per_km": float,
        "x_ohm_per_km": float,
        "c_nf_per_km": float,
        "g_us_per_km": float,
        "max_i_ka": float,
        "df": float,
        "parallel": int,
        "type": str,
        "in_service": bool,
        "max_loading_percent": float,
        "std_type": str
    },
    "trafo": {
        "name": str,
        "std_type": str,
        "hv_bus": int,
        "lv_bus": int,
        "sn_mva": float,
        "vn_hv_kv": float,
        "vn_lv_kv": float,
        "vk_percent": float,
        "vkr_percent": float,
        "pfe_kw": float,
        "i0_percent": float,
        "shift_degree": float,
        "tap_side": str,
        "tap_neutral": int,
        "tap_min": int,
        "tap_max": int,
        "tap_step_percent": float,
        "tap_step_degree": float,
        "tap_pos": int,
        "tap_phase_shifter": bool,
        "parallel": int,
        "df": float,
        "in_service": bool
    },
    "motor": {
        "name": str,
        "bus": int,
        "pn_mech_mw": float,
        "loading_percent": float,
        "cos_phi": float,
        "cos_phi_n": float,
        "efficiency_percent": float,
        "efficiency_n_percent": float,
        "lrc_pu": float,
        "vn_kv": float,
        "scaling": float,
        "in_service": bool,
        "rx": float
    },
    "asymmetric_load": {
        "name": str,
        "bus": int,
        "p_a_mw": float,
        "q_a_mvar": float,
        "p_b_mw": float,
        "q_b_mvar": float,
        "p_c_mw": float,
        "q_c_mvar": float,
        "sn_mva": float,
        "scaling": float,
        "in_service": bool,
        "type": str
    },
    "asymmetric_sgen": {
        "name": str,
        "bus": int,
        "p_a_mw": float,
        "q_a_mvar": float,
        "p_b_mw": float,
        "q_b_mvar": float,
        "p_c_mw": float,
        "q_c_mvar": float,
        "sn_mva": float,
        "scaling": float,
        "in_service": bool,
        "type": str,
        "current_source": bool
    },
    "storage": {
        "name": str,
        "bus": int,
        "p_mw": float,
        "q_mvar": float,
        "sn_mva": float,
        "soc_percent": float,
        "min_e_mwh": float,
        "max_e_mwh": float,
        "scaling": float,
        "in_service": bool,
        "type": str
    },
    "shunt": {
        "bus": int,
        "name": str,
        "q_mvar": float,
        "p_mw": float,
        "vn_kv": float,
        "step": int,
        "max_step": int,
        "in_service": bool
    },
    "trafo3w": {
        "name": str,
        "std_type": str,
        "hv_bus": int,
        "mv_bus": int,
        "lv_bus": int,
        "sn_hv_mva": float,
        "sn_mv_mva": float,
        "sn_lv_mva": float,
        "vn_hv_kv": float,
        "vn_mv_kv": float,
        "vn_lv_kv": float,
        "vk_hv_percent": float,
        "vk_mv_percent": float,
        "vk_lv_percent": float,
        "vkr_hv_percent": float,
        "vkr_mv_percent": float,
        "vkr_lv_percent": float,
        "pfe_kw": float,
        "i0_percent": float,
        "shift_mv_degree": float,
        "shift_lv_degree": float,
        "tap_side": str,
        "tap_neutral": int,
        "tap_min": int,
        "tap_max": int,
        "tap_step_percent": float,
        "tap_step_degree": float,
        "tap_pos": int,
        "tap_at_star_point": bool,
        "in_service": bool,
    },
    "impedance": {
        "name": str,
        "from_bus": int,
        "to_bus": int,
        "rft_pu": float,
        "xft_pu": float,
        "rtf_pu": float,
        "xtf_pu": float,
        "sn_mva": float,
        "in_service": bool
    },
    "dcline": {
        "name": str,
        "from_bus": int,
        "to_bus": int,
        "p_mw": float,
        "loss_percent": float,
        "loss_mw": float,
        "vm_from_pu": float,
        "vm_to_pu": float,
        "max_p_mw": float,
        "min_q_from_mvar": float,
        "min_q_to_mvar": float,
        "max_q_from_mvar": float,
        "max_q_to_mvar": float,
        "in_service": bool
    },
    "ward": {
        "name": str,
        "bus": int,
        "ps_mw": float,
        "qs_mvar": float,
        "qz_mvar": float,
        "pz_mw": float,
        "in_service": bool
    },
    "xward": {
        "name": str,
        "bus": int,
        "ps_mw": float,
        "qs_mvar": float,
        "qz_mvar": float,
        "pz_mw": float,
        "r_ohm": float,
        "x_ohm": float,
        "vm_pu": float,
        "slack_weight": float,
        "in_service": bool
    },
    "measurement": {
        "name": str,
        "measurement_type": str,
        "element_type": str,
        "element": int,
        "value": float,
        "std_dev": float,
        "side": str
    },
    "pwl_cost": {
        "power_type": str,
        "element": int,
        "et": str,
        "points": str
    },
    "poly_cost": {
        "element": int,
        "et": str,
        "cp0_eur": float,
        "cp1_eur_per_mw": float,
        "cp2_eur_per_mw2": float,
        "cq0_eur": float,
        "cq1_eur_per_mvar": float,
        "cq2_eur_per_mvar2": float
    },
    'characteristic': {
        'object': object
    },
    'controller': {
        'object': object,
        'in_service': bool,
        'order': float,
        'level': str,
        'initial_run': bool,
        "recycle": str
    },
    "line_geodata": {
        "coords": object
    },
    "bus_geodata": {
        "x": float,
        "y": float,
        "coords": object
    },
}

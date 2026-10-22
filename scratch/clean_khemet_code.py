# -*- coding: utf-8 -*-
with open("scripts/world/alto_west_cais.gd", "r", encoding="utf-8") as f:
    text = f.read()

# Bloco antigo a ser substituído pela composição limpa, vasta e solene
old_block = '''\t# -------------------------------------------------------------------------
\t# 8. SÍTIOS ARQUEOLÓGICOS & CALÇADA IMPERIAL PAVIMENTADA DE KHEMET-RA
\t# -------------------------------------------------------------------------
\tvar ruins_data: Array[Dictionary] = [
\t\t{"pos": Vector2(-6200, -1150),  "scale": Vector2(0.68, 0.62), "rot": 0.03,  "flip": false},
\t\t{"pos": Vector2(-9600, -1350),  "scale": Vector2(0.75, 0.68), "rot": -0.02, "flip": true},
\t\t{"pos": Vector2(-10800, -1450), "scale": Vector2(0.82, 0.74), "rot": 0.02,  "flip": false},
\t\t{"pos": Vector2(-11400, -1520), "scale": Vector2(0.86, 0.78), "rot": -0.03, "flip": true},
\t\t{"pos": Vector2(-11800, -1530), "scale": Vector2(0.88, 0.80), "rot": 0.02,  "flip": false},
\t\t{"pos": Vector2(-12200, -1500), "scale": Vector2(0.85, 0.76), "rot": -0.02, "flip": true},
\t\t{"pos": Vector2(-12600, -1490), "scale": Vector2(0.88, 0.78), "rot": 0.03,  "flip": false},
\t\t{"pos": Vector2(-13000, -1470), "scale": Vector2(0.90, 0.80), "rot": -0.02, "flip": true},
\t\t{"pos": Vector2(-13400, -1520), "scale": Vector2(0.88, 0.78), "rot": 0.02,  "flip": false},
\t\t{"pos": Vector2(-13800, -1560), "scale": Vector2(0.92, 0.82), "rot": -0.03, "flip": true},
\t\t{"pos": Vector2(-14250, -1580), "scale": Vector2(0.95, 0.85), "rot": 0.00,  "flip": false},
\t\t{"pos": Vector2(-14650, -1620), "scale": Vector2(0.92, 0.82), "rot": 0.02,  "flip": true},
\t\t{"pos": Vector2(-15000, -1720), "scale": Vector2(0.90, 0.80), "rot": -0.02, "flip": false},
\t\t{"pos": Vector2(-15400, -1850), "scale": Vector2(0.92, 0.82), "rot": 0.03,  "flip": true},
\t\t{"pos": Vector2(-15800, -1960), "scale": Vector2(0.95, 0.85), "rot": -0.02, "flip": false},
\t\t{"pos": Vector2(-16250, -2000), "scale": Vector2(1.00, 0.88), "rot": 0.02,  "flip": true}
\t]
\tfor r_info in ruins_data:
\t\t_place_khemet_ruins(ruins_group, root, r_info["pos"], r_info["scale"], r_info["rot"], r_info["flip"])

\t# -------------------------------------------------------------------------
\t# 9. OBELISCO MONUMENTAL TOMBADO DE KHEMET-RA
\t# -------------------------------------------------------------------------
\t_place_khemet_obelisk(cliffs_group, root, Vector2(-6700, -1250), Vector2(0.72, 0.68), 0.02)

\t# -------------------------------------------------------------------------
\t# 10. COLOSSO AUTÔMATO PRECURSOR SOTERRADO (O Guardião de Khemet-Ra)
\t# -------------------------------------------------------------------------
\t_place_khemet_colossus(cliffs_group, root, Vector2(-10400, -1480), Vector2(0.85, 0.80))

\t# -------------------------------------------------------------------------
\t# 11. POÇO DE MEMÓRIA SOLAR & NEXUS PRECURSOR DE KHEMET-RA
\t# -------------------------------------------------------------------------
\t_place_khemet_memory_well(cliffs_group, root, Vector2(-11600, -1550), Vector2(0.95, 0.90))

\t# 4 Braseiros Cerimoniais em volta do Poço de Memória Solar
\t_place_khemet_brazier(cliffs_group, root, Vector2(-11820, -1650), Vector2(0.62, 0.58))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-11380, -1650), Vector2(0.62, 0.58))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-11820, -1450), Vector2(0.62, 0.58))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-11380, -1450), Vector2(0.62, 0.58))

\t# -------------------------------------------------------------------------
\t# 12. AVENIDA DAS ESFINGES PROCESSIONAIS (Flanqueando a Calçada Imperial)
\t# -------------------------------------------------------------------------
\tvar avenue_sphinxes: Array[Dictionary] = [
\t\t# Par 1: Entrada da Avenida
\t\t{"pos": Vector2(-12150, -1640), "scale": Vector2(0.65, 0.60), "flip": false},
\t\t{"pos": Vector2(-12150, -1360), "scale": Vector2(0.65, 0.60), "flip": true},
\t\t# Par 2: Meio da Avenida
\t\t{"pos": Vector2(-12750, -1640), "scale": Vector2(0.68, 0.62), "flip": false},
\t\t{"pos": Vector2(-12750, -1350), "scale": Vector2(0.68, 0.62), "flip": true},
\t\t# Par 3: Próximo à Grande Esfinge
\t\t{"pos": Vector2(-13450, -1670), "scale": Vector2(0.70, 0.64), "flip": false},
\t\t{"pos": Vector2(-13450, -1370), "scale": Vector2(0.70, 0.64), "flip": true},
\t\t# Par 4: Antes do Portal do Pilone
\t\t{"pos": Vector2(-13980, -1690), "scale": Vector2(0.72, 0.65), "flip": false},
\t\t{"pos": Vector2(-13980, -1390), "scale": Vector2(0.72, 0.65), "flip": true}
\t]
\tfor s_data in avenue_sphinxes:
\t\t_place_khemet_avenue_sphinx(cliffs_group, root, s_data["pos"], s_data["scale"], s_data["flip"])

\t# -------------------------------------------------------------------------
\t# 13. ESTELAS SAGRADAS COM CRISTAIS SOLARES (Balizas Luminosas na Calçada)
\t# -------------------------------------------------------------------------
\tvar steles_data: Array[Dictionary] = [
\t\t{"pos": Vector2(-11900, -1620), "scale": Vector2(0.65, 0.60), "flip": false},
\t\t{"pos": Vector2(-12450, -1370), "scale": Vector2(0.68, 0.62), "flip": true},
\t\t{"pos": Vector2(-13100, -1650), "scale": Vector2(0.70, 0.64), "flip": false},
\t\t{"pos": Vector2(-13700, -1380), "scale": Vector2(0.72, 0.65), "flip": true},
\t\t{"pos": Vector2(-14550, -1720), "scale": Vector2(0.72, 0.65), "flip": false},
\t\t{"pos": Vector2(-15250, -1850), "scale": Vector2(0.75, 0.68), "flip": true},
\t\t{"pos": Vector2(-15950, -2100), "scale": Vector2(0.78, 0.70), "flip": false}
\t]
\tfor st_data in steles_data:
\t\t_place_khemet_stele(cliffs_group, root, st_data["pos"], st_data["scale"], st_data["flip"])

\t# -------------------------------------------------------------------------
\t# 14. COLUNATAS E PÓRTICOS EM RUÍNAS
\t# -------------------------------------------------------------------------
\tvar columns_data: Array[Dictionary] = [
\t\t{"pos": Vector2(-12350, -1720), "scale": Vector2(0.76, 0.72), "rot": 0.02,  "flip": false},
\t\t{"pos": Vector2(-12950, -1310), "scale": Vector2(0.78, 0.74), "rot": -0.03, "flip": true},
\t\t{"pos": Vector2(-13600, -1740), "scale": Vector2(0.82, 0.76), "rot": 0.04,  "flip": false},
\t\t{"pos": Vector2(-14550, -1450), "scale": Vector2(0.84, 0.78), "rot": -0.02, "flip": true},
\t\t{"pos": Vector2(-14800, -1820), "scale": Vector2(0.86, 0.80), "rot": 0.03,  "flip": false},
\t\t{"pos": Vector2(-15600, -1750), "scale": Vector2(0.90, 0.82), "rot": -0.03, "flip": true}
\t]
\tfor col_info in columns_data:
\t\t_place_khemet_columns(cliffs_group, root, col_info["pos"], col_info["scale"], col_info["rot"], col_info["flip"])

\t# -------------------------------------------------------------------------
\t# 15. A GRANDE ESFINGE GUARDIÃ COLOSSAL (O Coração da Praça Imperial)
\t# -------------------------------------------------------------------------
\t_place_khemet_sphinx(cliffs_group, root, Vector2(-13050, -1480), Vector2(0.95, 0.88), false)
\t_place_khemet_brazier(cliffs_group, root, Vector2(-13280, -1420), Vector2(0.68, 0.62))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-12820, -1420), Vector2(0.68, 0.62))

\t# -------------------------------------------------------------------------
\t# 16. O PILONE / PORTAL MONUMENTAL DO TEMPLO DE KHEMET-RA
\t# -------------------------------------------------------------------------
\t_place_khemet_temple_gate(cliffs_group, root, Vector2(-14250, -1580), Vector2(1.05, 0.98))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-14480, -1530), Vector2(0.72, 0.66))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-14020, -1530), Vector2(0.72, 0.66))

\t# -------------------------------------------------------------------------
\t# 17. SARCÓFAGOS E RELICÁRIOS DE AUTÔMATOS (Mecânica e Tumbas Pré-Cataclismo)
\t# -------------------------------------------------------------------------
\tvar sarcophagus_data: Array[Dictionary] = [
\t\t{"pos": Vector2(-10600, -1420), "scale": Vector2(0.68, 0.62), "rot": 0.05,  "flip": false},
\t\t{"pos": Vector2(-11750, -1720), "scale": Vector2(0.72, 0.66), "rot": -0.04, "flip": true},
\t\t{"pos": Vector2(-14850, -2120), "scale": Vector2(0.75, 0.68), "rot": 0.06,  "flip": false},
\t\t{"pos": Vector2(-15350, -2050), "scale": Vector2(0.78, 0.70), "rot": -0.05, "flip": true},
\t\t{"pos": Vector2(-16050, -1880), "scale": Vector2(0.82, 0.74), "rot": 0.04,  "flip": false},
\t\t{"pos": Vector2(-16650, -1960), "scale": Vector2(0.85, 0.76), "rot": -0.06, "flip": true}
\t]
\tfor sarc_info in sarcophagus_data:
\t\t_place_khemet_sarcophagus(cliffs_group, root, sarc_info["pos"], sarc_info["scale"], sarc_info["rot"], sarc_info["flip"])

\t# -------------------------------------------------------------------------
\t# 18. A RAMPA CERIMONIAL DA NECRÓPOLE SUBTERRÂNEA
\t# -------------------------------------------------------------------------
\t_place_khemet_necropolis_ramp(cliffs_group, root, Vector2(-15100, -2100), Vector2(0.95, 0.90))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-15320, -2040), Vector2(0.70, 0.64))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-14880, -2040), Vector2(0.70, 0.64))

\t# -------------------------------------------------------------------------
\t# 19. A GRANDE PIRÂMIDE PRECURSORA SOTERRADA DE KHEMET-RA (MONUMENTO TITÂNICO)
\t# -------------------------------------------------------------------------
\t_place_khemet_great_pyramid(cliffs_group, root, Vector2(-16300, -2020), Vector2(1.35, 1.25))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-16650, -1880), Vector2(0.78, 0.70))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-15950, -1880), Vector2(0.78, 0.70))'''

new_block = '''\t# -------------------------------------------------------------------------
\t# 8. SÍTIOS ARQUEOLÓGICOS ISOLADOS (Lajes semi-soterradas pelo vento)
\t# -------------------------------------------------------------------------
\tvar ruins_data: Array[Dictionary] = [
\t\t{"pos": Vector2(-6200, -1150),  "scale": Vector2(0.68, 0.62), "rot": 0.03,  "flip": false},
\t\t{"pos": Vector2(-10800, -1450), "scale": Vector2(0.82, 0.74), "rot": -0.02, "flip": true}
\t]
\tfor r_info in ruins_data:
\t\t_place_khemet_ruins(ruins_group, root, r_info["pos"], r_info["scale"], r_info["rot"], r_info["flip"])

\t# -------------------------------------------------------------------------
\t# 9. OBELISCO MONUMENTAL TOMBADO DE KHEMET-RA (Marco Solitário no Deserto)
\t# -------------------------------------------------------------------------
\t_place_khemet_obelisk(cliffs_group, root, Vector2(-6700, -1250), Vector2(0.72, 0.68), 0.02)

\t# -------------------------------------------------------------------------
\t# 10. MARCO 1: COLOSSO AUTÔMATO SOTERRADO (O Guardião Ancestral na Areia)
\t# -------------------------------------------------------------------------
\t_place_khemet_colossus(cliffs_group, root, Vector2(-10400, -1480), Vector2(0.85, 0.80))

\t# -------------------------------------------------------------------------
\t# 11. MARCO 2: POÇO DE MEMÓRIA SOLAR (Santuário Místico Isolado nas Dunas)
\t# -------------------------------------------------------------------------
\t_place_khemet_memory_well(cliffs_group, root, Vector2(-11800, -1550), Vector2(0.95, 0.90))

\t# -------------------------------------------------------------------------
\t# 12. MARCO 3: A GRANDE ESFINGE GUARDIÃ (Escultura Colossal Solitária na Rocha)
\t# -------------------------------------------------------------------------
\t_place_khemet_sphinx(cliffs_group, root, Vector2(-13200, -1460), Vector2(0.95, 0.88), false)

\t# -------------------------------------------------------------------------
\t# 13. MARCO 4: O PILONE / PORTAL MONUMENTAL DO TEMPLO (Limiar Ciclópico)
\t# -------------------------------------------------------------------------
\t_place_khemet_temple_gate(cliffs_group, root, Vector2(-14600, -1580), Vector2(1.05, 0.98))

\t# -------------------------------------------------------------------------
\t# 14. MARCO 5: A RAMPA DA NECRÓPOLE SUBTERRÂNEA (Descida Sombria na Falésia)
\t# -------------------------------------------------------------------------
\t_place_khemet_necropolis_ramp(cliffs_group, root, Vector2(-15800, -2100), Vector2(0.95, 0.90))

\t# -------------------------------------------------------------------------
\t# 15. MARCO 6: A GRANDE PIRÂMIDE PRECURSORA SOTERRADA (O Ápice do Horizonte)
\t# -------------------------------------------------------------------------
\t_place_khemet_great_pyramid(cliffs_group, root, Vector2(-17000, -2020), Vector2(1.35, 1.25))'''

if old_block in text:
    text = text.replace(old_block, new_block, 1)
    with open("scripts/world/alto_west_cais.gd", "w", encoding="utf-8") as f:
        f.write(text)
    print("Sucesso! Código limpo e espaçado com protagonismo natural!")
else:
    print("Aviso: Bloco exato não encontrado!")

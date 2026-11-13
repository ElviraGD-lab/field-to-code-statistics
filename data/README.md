# Data passport

The data are not stored in this repository. This file says, for every dataset the book uses, where it comes from, under which licence, when it was downloaded and how to get it again.

The working coordinate system of the book is **ETRS89 / UTM zone 30N (EPSG:25830)**. Layers stored in WGS 84 (EPSG:4326) are reprojected in the code before any distance or area is measured.

Status of each entry: **checked** (source, licence and file verified) or **to check** (to be verified before the first chapter that uses it).

| Dataset | Source | Licence and attribution | Downloaded | Chapters | Status |
|---|---|---|---|---|---|
| Towers and spans of the 400 kV lines at the Pajares pass (33 towers, 34 spans) | Pajares project: OpenStreetMap topology, positions checked on PNOA orthophoto and LiDAR | derived data, CC BY 4.0; © OpenStreetMap contributors (ODbL); «PNOA cedido por © Instituto Geográfico Nacional» | 2026-10-17 | to be set | to check |
| Digital terrain model MDT02, Pajares (2 m) | CNIG / IGN, Centro de Descargas | CC BY 4.0: «Obra derivada de MDT02-cob2 2015-2021 CC-BY 4.0 scne.es» | 2026-09 | to be set | to check |
| PNOA LiDAR, 3rd coverage (Asturias 2024, Castilla y León 2025) and DTM 1 m derived from it | CNIG / IGN | CC BY 4.0: «PNOA cedido por © Instituto Geográfico Nacional» | 2026-10 | to be set | to check |
| Active fire detections, Spain 2012–2026: VIIRS S-NPP (request 810761), VIIRS NOAA-20 (839330), MODIS C6.1 (839329) | NASA FIRMS, https://firms.modaps.eosdis.nasa.gov/download/ | open data; acknowledgement: «We acknowledge the use of data and/or imagery from NASA's Fire Information for Resource Management System (FIRMS) (https://earthdata.nasa.gov/firms), part of NASA's Earth Science Data and Information System (ESDIS).» | 2026-09/10 | to be set | to check |
| Municipalities of Asturias (78 concejos) | OpenStreetMap, Geofabrik extract of Asturias, 2026-09-15 | ODbL: © OpenStreetMap contributors | 2026-09-15 | to be set | to check |
| Roads, places, land use and waterways of Asturias and Lena | OpenStreetMap, Geofabrik extract, 2026-09-15 | ODbL: © OpenStreetMap contributors | 2026-09-15 | to be set | to check |
| Power lines and towers of Asturias | OpenStreetMap | ODbL: © OpenStreetMap contributors | 2026-09-25 / 2026-10-04 | to be set | to check |
| Service continuity indices TIEPI and NIEPI by zone type, Spain | MITECO | to check | 2026-10 | to be set | to check |
| National Forest Inventory IFN4: Asturias, León, A Coruña | MITECO | to check | 2026-11 | to be set | to check |
| ICP Forests level I and II plots, Spain (tree heights and growth) | MITECO, Red de Seguimiento ICP Forests | to check | 2026-11 | to be set | to check |
| Weather station records, Asturias | AEMET OpenData (API key) | AEMET, attribution required | not yet | to be set | to check |

Each chapter script states at the top which of these files it reads.

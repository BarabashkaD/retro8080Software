# Provenance: rk86/collections/pyhonin-1999

A collection of game programs for the Radio-86RK in tape-file form (26 `.GAM`, 22 `.RKR`), with
its own notes, and `bios.rk`. Kept byte for byte as found.

## Origin

- Copied from the Karabas core fork, https://github.com/BarabashkaD/karabas-go-core-rk86 (a fork
  of https://github.com/andykarpov/karabas-go-core-rk86, where these files first appeared), commit
  `35e86e7`, path `pk/`. The files are the same at `d995355` (the fork reference of the layout
  migration).
- Taken with `git filter-repo --path pk/ --path-rename pk/:rk86/collections/pyhonin-1999/` on a
  fresh clone of the fork. In the upstream repo two commits carry them: its first commit
  (`bios.rk`) and the commit that added the other 51 files.
- The collection's own notes, kept as they are (CP866 text, CR LF line ends):
  - `FILE_ID.DIZ`: the collection's title and its date, 04.01.99.
  - `GR_1.TXT`: the compiler's notes, the credits for the programs and the publication date
    (04.01.99), signed by the compiler (V. Pyhonin; the folder is named after him and the year).
  - `DESCRIPT.ION`: one line per program, the file name and the game title (the game titles: see
    `DESCRIPT.ION`).
- `bios.rk` is not listed in `DESCRIPT.ION` and came in a separate, earlier commit; whether it was
  part of the 1999 collection is not stated.

## Licence

None stated by the authors; redistributed as found in the public fork. These files are not
relicensed by this repo's `NOTICE`; this `PROVENANCE.md` is the owner's doc (CC BY 4.0).

## Files

| File | Size | SHA-256 |
|---|---|---|
| `BOMBER.GAM` | 4106 | `50d07082ed141692d13bbeb82e949d493f84afb580e10739a207d992f3e8aa01` |
| `CHERV.RKR` | 2170 | `6790c22a0665c6574af498f4501d6513b00fae8d05d3baf7eb462658fef8bbfa` |
| `CHESS.GAM` | 28939 | `a00534d2b48ce261cf5cf6599295b77b225ed3a03e621f55a4137d5179d06836` |
| `CIRCUS.RKR` | 7657 | `3e60773027335b6a3942ca2112e45dd5a8b3a9d413c3899aac2da0a6fe6a9d24` |
| `DESCRIPT.ION` | 1188 | `aa25ae509eb16995344ff07e8a43a13c763b619cd8e07e58650a19a90d330d42` |
| `DIVERSE.GAM` | 5914 | `6c2152e695f69cec234f1cf8243ce8bfd4f92700890b29af31cccec0b80edf36` |
| `FILE_ID.DIZ` | 74 | `4410ec7716a7d8c0e62fbbf44dafb0d96c3ce1b8f2e1c68fae7d1917ca4499aa` |
| `GFIRE.GAM` | 11290 | `07ce2d17caf4a8c3ac16db9ff7b0e09cae726737000c37ac79048af8acb01021` |
| `GLASS1.GAM` | 1544 | `104024679449f57e10615e78f179df4661f063569761ff14a6df29cc9771b18f` |
| `GLASS2.GAM` | 2313 | `d9d63ac1bfd9d5c3789b987c77f0a86249081bbcfa7400d6e4ecdfaf6980abde` |
| `GR_1.TXT` | 395 | `e244dd455596359dccfd4e64e87d3600db2cf644a86e61fac33e31dce151dd55` |
| `KRESTNO.GAM` | 5131 | `ec67e8ebbb6d7beab5ec6fbb68932ff12e586a48c2159bf755e0acd0ae08d32b` |
| `KRESTNO.RKR` | 5187 | `c412aedd593988b2f858aa4d9f5b2639892b626906224c238a230960d1a9911c` |
| `KROK.GAM` | 6922 | `4cda9812846fc0d2fc6480efe5218ede319c1238769c3be9006edfbd62773781` |
| `LABYRINT.GAM` | 7967 | `c9022551f6bb3bc2a59c251671ecd5a006e0258a334e61b350e6f0a49ea57fc5` |
| `LEST.RKR` | 1643 | `aff85054cb023eb2a794759a5f87f07f619445cc7629cf62a53e38a035b3996a` |
| `LESTN1.RKR` | 7977 | `c863fa46c929d806763a35b1300369ddbf4dd349d20019ffabed84400b664c1e` |
| `LORUNNER.GAM` | 12554 | `4fc201ca9f94ff7b444c12446e0f8ee034f6e70da104b3ee73623857a0cf6367` |
| `MAZE.GAM` | 7946 | `51bc51462c96fec48b0ab1e117f86a1a4744a835953977094f9e824489eb9e1c` |
| `PACMAN.GAM` | 4543 | `b54211e1c7d16d564ee16bdff3037bca050ad6ea308467a6486b40d436e81934` |
| `PACMAN.RKR` | 9830 | `a3a3976ed70791c7929ed67bb7ce400ffc6b463fd1091a36ca0682a918ddb13c` |
| `PACMAN1.GAM` | 9819 | `7e4081bb1470b73e3d352539e2a23349bae9dec52efb958cab9ffc1c47b04150` |
| `PAKET.RKR` | 16075 | `a2fef3aeaff7d32f4c74e87070589d95c63f702fc67e57f79a055768aeea36c7` |
| `PAKET2.RKR` | 16623 | `6460fe009ea0f7bcc8c0b240c09f1bc3cd94fabe05dfdbb8f4988e6c318b23c3` |
| `PINGPONG.RKR` | 2945 | `bea9cfb64e6827f7e72f3ebfeb87e3cf201697544ba95da6b1240ef287e7725e` |
| `PITON.GAM` | 520 | `049e4cfa3a3e8f5e8cdaa7ff61a7db811c1c85921d74cdc256e10620bc30356c` |
| `PUSHER.GAM` | 1198 | `a164dfd1cae2b2c220cc6136bc485c72eaa8354a8909ca98269348dc305bbef7` |
| `PVO.RKR` | 1291 | `651ad67856eb5f3a9983dc434e826d3d068d20f82a3890d9244285ad70c127a9` |
| `RIKOSHET.RKR` | 12248 | `b2ce88d814e51a50aa44b0ec27c83fba5ed7a45def3de95398ef0c36a884460a` |
| `SDEMISE.GAM` | 6291 | `a9e564947f661863e7a404bda8df6861f5313699d2afd2b33530e9abe06886b8` |
| `SKACHKI.GAM` | 1288 | `ccf797adc5691d789abb632de9fdbe0514c112c4f5e880a02d110f402e49e148` |
| `SKVOTCH.RKR` | 716 | `9cc5448578975c5df468fb6053085af2b34f55baae0c9885a4a8fd92ba9d3898` |
| `SLAMS.RKR` | 3848 | `9bbbf7c3e4d570440817e044137992f933623e4f47e0267981a3b02a4b937839` |
| `SOS1.GAM` | 4106 | `d6b06a3c2700c24a35c49d51e3ad9d3a3e66c0129d4f58d4c3e369dbba93b8fd` |
| `SOS2.GAM` | 3307 | `eed977c742fe6063bb414d5394ba70e9a16e62cbf6e3a68ef964b9e015723a04` |
| `SPITON.GAM` | 16154 | `eb5a01764018c7958c635f32c80670599ff7694a3065ee8f0ea5822a80ed7ce9` |
| `STRANGER.GAM` | 4139 | `d6955d9c48aae29c843b41c73835970f644548875a57a9891e6a52582dfc6c0b` |
| `TAPPER.GAM` | 4106 | `46a4631382449d054cfd10cf73d0d0217aebd8ce481f80c09c8e49cf679799fb` |
| `TENNIS.GAM` | 4949 | `5d1a2f08d9cd1ea55952d51774cc9fec3cf2203ae999ad3d5a9b0e01ba5f9a21` |
| `TETR2.RKR` | 3212 | `b893bed425d0e8bde891ddfe6faf7e91b648dfd3c1e4c3d0b4615626fc956ed4` |
| `TETRIS1.RKR` | 1288 | `ee3273b7e83d57245942fb29f566c383f8893b61115115e4dcd0099a40c5f8f6` |
| `TETRIS4.RKR` | 1644 | `20e8ba94e90e691e80c93d1542c70974c4cbbe02a0dec1c7349c3fa0a72e737a` |
| `TOCHKI.RKR` | 1185 | `8ce8a0ae66e9f06acbdf27198610e09aa38afad8efda277cd2230d333f96559f` |
| `UDAW.GAM` | 2058 | `067f820fa10cd74f5401be975cf6ee9db1385e19c3ede7773b05f182efd2c224` |
| `UTKA.GAM` | 1851 | `9de31ee3fe8a115afcfaa62c513328162d99478d66c3c57b54f54fa94620a198` |
| `VOLCANO.RKR` | 4089 | `caf87451d24992347132b28baad1260f51564819c7ba64cb154941663ff1c956` |
| `XONIX.RKR` | 1995 | `b0686edfbd3b2c50245da0e371d80551331c7ee0acbfe72acaa1481713a5cb27` |
| `XONIX1.RKR` | 2828 | `f065e486d019b37c479c17c8fa01984b070114ab6b62c53c0204e02efb9015f6` |
| `XONIXZM.GAM` | 3832 | `042ce793f226b84c78e6fb095e88f4a78127ed2df249240dd38d25fbaa22ae47` |
| `ZAGIB.RKR` | 1035 | `7182620d6d8e9311f1aac6a0bf632782f54dd0dee4dea94e841c396d66d8688d` |
| `ZMEI.RKR` | 4250 | `2868180b648e544c7321b11e77ebbfeca98360c7f5da83c05c5dafc204a76e45` |
| `bios.rk` | 4106 | `56fb9391389886e7f4ba55f259bb27a8653b0a50216b0fac056e3da0698433b1` |

const fs = require('fs');
const path = require('path');
const sharp = require('C:/Users/Usuario/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const root = path.resolve(__dirname, '..');
sharp(fs.readFileSync(path.join(root, 'docs/alto-lixo-planta-espacial.svg')))
  .png()
  .toFile(path.join(root, 'docs/alto-lixo-planta-espacial.png'))
  .then(info => console.log('RENDER', info.width, info.height))
  .catch(error => { console.error(error); process.exitCode = 1; });

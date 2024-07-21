const path = require('path');

module.exports = {
    webpack: {
        alias: {
            '@': path.resolve(__dirname, 'src'),
        },
        extensions: [
            '.ts',
            '.tsx',
            '.jsx',
            '.js',
            '.json'
        ],
    },
};
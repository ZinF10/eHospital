module.exports = function (api) {
    api.cache(true);
    return {
        presets: ['babel-preset-expo'],
        plugins: [
            [
                'babel-plugin-module-resolver',
                {
                    root: ['./src/'],
                    alias: {
                        '@/*': './src/*',
                    },
                    extensions: ['.js', '.jsx', '.ts', '.tsx'],
                },
            ],
            [
                'module:react-native-dotenv',
                {
                    envName: 'APP_ENV',
                    moduleName: '@env',
                    path: '.env',
                },
            ],
            'react-native-reanimated/plugin',
        ],
    };
};

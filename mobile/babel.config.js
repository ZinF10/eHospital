module.exports = {
  presets: ['module:@react-native/babel-preset'],
  plugins: [
    [
      'babel-plugin-module-resolver',
      {
        root: ['./src/'],
        alias: {
          "*": ["./src/*"],
          "@components": ["./src/components/*"],
          "@themes": ["./src/themes/*"],
          "@screens": ["./src/screens/*"],
          "@routes": ["./src/routes/*"],
          "@assets": ["./src/assets/*"],
          "@hooks": ["./src/hooks/*"],
          "@services": ["./src/services/*"]
        },
        extensions: [
          '.ios.ts',
          '.android.ts',
          '.ts',
          '.ios.tsx',
          '.android.tsx',
          '.tsx',
          '.jsx',
          '.js',
          '.json',
        ],
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
    'react-native-reanimated/plugin'
  ],
};

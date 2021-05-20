const BundleTracker = require('webpack-bundle-tracker');

const PORT = process.env.LOCAL_WEBPACK_SERVER_PORT || '3000';
const localhost = `http://localhost:${PORT}/`

process.env.WDS_SOCKET_PORT = PORT;

module.exports = {
  reactScriptsVersion: 'react-scripts',
  webpack: {
    plugins: {
      add: [
        new BundleTracker({
          path: __dirname,
          filename: '../client/webpack-stats.json',
        }),
      ],
    },
    configure: (config) => ({
      ...config,
      output: {
        ...config.output,
        publicPath: process.env.NODE_ENV === 'production' ? '/' : localhost,
      },
    }),
  },
  devServer: {
    headers: { 'Access-Control-Allow-Origin': ['*'] }
    
  },
};

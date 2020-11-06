const BundleTracker = require("webpack-bundle-tracker");

const pages = {
    'clientapp': {
        entry: './src/main.ts',
        chunks: ['chunk-vendors'],
    },
}

const PORT = process.env.LOCAL_WEBPACK_SERVER_PORT || '8080'
const DEVSERVER_HOST = process.env.DEVSERVER_HOST || 'localhost';
const localhost = `http://localhost:${PORT}/`

module.exports = {
  pages: pages,
  transpileDependencies: ["vuetify"],
  filenameHashing: false,
  productionSourceMap: false,
  publicPath: process.env.NODE_ENV === 'production' ? '' : localhost,
  outputDir: '../artistry_codex/static/client/',

  chainWebpack: config => {

      config.optimization
          .splitChunks({
              cacheGroups: {
                  vendor: {
                      test: /[\\/]node_modules[\\/]/,
                      name: "chunk-vendors",
                      chunks: "all",
                      priority: 1
                  },
              },
          });

      Object.keys(pages).forEach(page => {
          config.plugins.delete(`html-${page}`);
          config.plugins.delete(`preload-${page}`);
          config.plugins.delete(`prefetch-${page}`);
      })

      config
          .plugin('BundleTracker')
          .use(BundleTracker, [{filename: '../clientapp/webpack-stats.json'}]);

      config.resolve.alias
          .set('__STATIC__', 'static')

      config.devServer
          .public(localhost)
          .host(DEVSERVER_HOST)
          .port(PORT)
          .hotOnly(true)
          .watchOptions({poll: 1000})
          .https(false)
          .headers({"Access-Control-Allow-Origin": ["*"]})

  }
};

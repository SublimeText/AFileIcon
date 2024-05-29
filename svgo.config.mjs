export default {
    multipass: true,
    js2svg: {
        indent: 2,
        pretty: true,
    },
    plugins: [
        'removeDoctype',
        'removeXMLProcInst',
        'removeComments',
        'removeMetadata',
        'removeEditorsNSData',
        'cleanupAttrs',
        'cleanupIds',
        'cleanupNumericValues',
        'removeUselessDefs',
        'convertColors',
        'removeUnknownsAndDefaults',
        'removeNonInheritableGroupAttrs',
        {
            name: 'removeUselessStrokeAndFill',
            params: {
                removeNone: true,
            },
        },
        'removeDimensions',
        'cleanupEnableBackground',
        'removeHiddenElems',
        'removeEmptyText',
        'cleanupListOfValues',
        {
            name: 'convertShapeToPath',
            params: {
                convertArcs: true,
            },
        },
        'convertEllipseToCircle',
        'moveElemsAttrsToGroup',
        'moveGroupAttrsToElems',
        'collapseGroups',
        {
            name: 'convertPathData',
            params: {
                floatPrecision: 3,
                noSpaceAfterFlags: false,
            },
        },
        'convertTransform',
        'removeEmptyAttrs',
        'removeEmptyContainers',
        'removeUnusedNS',
        {
            name: 'mergePaths',
            params: {
                force: true,
                noSpaceAfterFlags: true,
            },
        },
        {
            name: 'addAttributesToSVGElement',
            params: {
                attributes: [{
                    'fill' :'#000',
                    'fill-rule': 'evenodd',
                    'viewBox': '0 0 16 16',
                    'xmlns': 'http://www.w3.org/2000/svg',
                }],
            },
        },
        {
            name: 'removeAttrs',
            params: {
                attrs: [
                    'svg:.*(?<!((xmlns)|(fill)|(fill-rule)|(viewBox)))',
                    'path:(?!d)',
                ],
            },
        },
        'sortAttrs',
        'sortDefsChildren',
        'removeOffCanvasPaths',
        'removeRasterImages',
        'removeStyleElement',
        'removeScriptElement',
        'removeTitle',
        'removeDesc',
    ],
};

const NEWLINE_INDENT_REGEX = /(?:\n(?:\s*))+/g;

function t(strings, ...values) {
    if (typeof strings === 'function') {
        return (...args) => t(['', ''], strings(...args));
    }
    if (!Array.isArray(strings)) {
        return t([strings]);
    }
    return strings
        .reduce((result, string, index) => result + values[index - 1] + string)
        .replace(NEWLINE_INDENT_REGEX, ' ')
        .trim();
}

const SVG_PATH_REGEX = /^m[-mzlhvcsqtae\d,. ]+$/i;

export default {
    rules: {
        elm: {
            'svg': 1,
            'svg > path': 1,
            '*': false,
        },
        attr: [
            {
                'fill' :'#000',
                'fill-rule': 'evenodd',
                'viewBox': '0 0 16 16',
                'xmlns': 'http://www.w3.org/2000/svg',
                'rule::selector': 'svg',
                'rule::whitelist': true,
                'rule::order': ['xmlns', 'fill', 'fill-rule', 'viewBox'],
            },
            {
                'd': SVG_PATH_REGEX,
                'rule::selector': 'svg > path',
                'rule::whitelist': true,
                'rule::order': true,
            },
        ],
        valid: true,
        custom: [
            (reporter, $, ast, { filename }) => {
                reporter.name = 'no-self-closing-path';

                // Don't allow explicit '</path>' closing tag
                if (!ast.source.includes('</path>')) {
                    return;
                }

                const index = ast.source.indexOf('</path>');
                const message = 'Invalid SVG content format';
                const reason = t`
                    found a closing "path" tag at index ${index}.
                    The path should be self-closing,
                    use "/>" instead of "></path>"
                `;
                reporter.error(`${message}: ${reason}`);
            },
        ]
    },
    ignore: [
        // TODO: go through these and simplify/remove fill paths;
        // I've barely skimmed all svgs so there are probably more
        'icons/svg/file_type_fsharp.svg',
        'icons/svg/file_type_nix.svg',
        'icons/svg/file_type_python.svg',
        'icons/svg/file_type_sublime.svg',
    ],
};

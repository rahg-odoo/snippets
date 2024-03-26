/** @odoo-module **/


import publicWidget from "@web/legacy/js/public/public_widget";
import { renderToElement } from "@web/core/utils/render";

export const Dynamic = publicWidget.Widget.extend({
    selector: '.dynamic_snippet_blog',
    /**
     * @constructor
     */
    init: function () {
        this._super.apply(this, arguments);
        this.rpc = this.bindService("rpc");
    },

    start: async function () {
        var self = this;
        var resultEl = self.el.querySelector('#replacing_with_other_div');
        const tickets = await self.rpc("/ticket-data-all")
        console.log(tickets)
        resultEl.replaceWith(renderToElement('snip.this_will_replace', {
            tickets: tickets
        }))
      
    },
});

publicWidget.registry.dynamic_snippet_blog = Dynamic;
return Dynamic;
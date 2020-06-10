import matplotlib.pyplot as plt
import mpld3
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpld3 import plugins, utils


class MousePositionDatePlugin(mpld3.plugins.PluginBase):
    """Plugin for displaying mouse position with a datetime x axis."""

    JAVASCRIPT = """
    mpld3.register_plugin("mousepositiondate", MousePositionDatePlugin);
    MousePositionDatePlugin.prototype = Object.create(mpld3.Plugin.prototype);
    MousePositionDatePlugin.prototype.constructor = MousePositionDatePlugin;
    MousePositionDatePlugin.prototype.requiredProps = [];
    MousePositionDatePlugin.prototype.defaultProps = {
    fontsize: 12,
    xfmt: "%Y-%m-%d %H:%M:%S",
    yfmt: ".3g"
    };
    function MousePositionDatePlugin(fig, props) {
    mpld3.Plugin.call(this, fig, props);
    }
    MousePositionDatePlugin.prototype.draw = function() {
    var fig = this.fig;
    var xfmt = d3.time.format(this.props.xfmt);
    var yfmt = d3.format(this.props.yfmt);
    var coords = fig.canvas.append("text").attr("class", "mpld3-coordinates").style("text-anchor", "end").style("font-size", this.props.fontsize).attr("x", this.fig.width - 5).attr("y", this.fig.height - 5);
    for (var i = 0; i < this.fig.axes.length; i++) {
      var update_coords = function() {
        var ax = fig.axes[i];
        return function() {
          var pos = d3.mouse(this);
          x = ax.xdom.invert(pos[0]);
          y = ax.ydom.invert(pos[1]);
          coords.text("(" + xfmt(x) + ", " + yfmt(y) + ")");
        };
      }();
      fig.axes[i].baseaxes.on("mousemove", update_coords).on("mouseout", function() {
        coords.text("");
      });
    }
    };
    """
    def __init__(self, fontsize=14, xfmt="%Y-%m-%d %H:%M:%S", yfmt=".3g"):
        self.dict_ = {"type": "mousepositiondate",
                      "fontsize": fontsize,
                      "xfmt": xfmt,
                      "yfmt": yfmt}

class BarLabelToolTip(plugins.PluginBase):    
    JAVASCRIPT = """
    mpld3.register_plugin("barlabeltoolTip", BarLabelToolTip);
    BarLabelToolTip.prototype = Object.create(mpld3.Plugin.prototype);
    BarLabelToolTip.prototype.constructor = BarLabelToolTip;
    BarLabelToolTip.prototype.requiredProps = ["ids","labels"];
    BarLabelToolTip.prototype.defaultProps = {
        hoffset: 0,
        voffset: 10,
        location: 'mouse'
    };
    function BarLabelToolTip(fig, props){
        mpld3.Plugin.call(this, fig, props);
    };
    
    BarLabelToolTip.prototype.draw = function(){
        var svg = d3.select("#" + this.fig.figid);
        var objs = svg.selectAll(".mpld3-path");
        var loc = this.props.location;
        var labels = this.props.labels
        
        test = this.fig.canvas.append("text")
            .text("hello world")
            .style("font-size", 72)
            .style("opacity", 0.5)
            .style("text-anchor", "middle")
            .attr("x", this.fig.width / 2)
            .attr("y", this.fig.height / 2)
            .style("visibility", "hidden");
        
        function mousemove(d) {
            if (loc === "mouse") {
                var pos = d3.mouse(this.fig.canvas.node())
                this.x = pos[0] + this.props.hoffset;
                this.y = pos[1] - this.props.voffset;
            }

            test
                .attr("x", this.x)
                .attr("y", this.y);
        };

        function mouseout(d) {
            test.style("visibility", "hidden")
        };
            
        this.props.ids.forEach(function(id, i) {
            
            
            var obj = mpld3.get_element(id);
            
            function mouseover(d) {
                test.style("visibility", "visible")
                    .style("font-size", 24)
                    .style("opacity", 0.7)
                    .text(labels[i])
            };
            
            obj.elements().on("mouseover", mouseover.bind(this))
                          
        });
            
       objs.on("mousemove", mousemove.bind(this)) 
           .on("mouseout", mouseout.bind(this));     
        
    }       
    """
    def __init__(self, ids, labels=None, location="mouse"):

        self.dict_ = {"type": "barlabeltoolTip",
                      "ids": ids,
                      "labels": labels,
                      "location": location}

fig, ax = plt.subplots()

dates = [datetime(2015, 9, 10), datetime(2015, 9, 11), datetime(2015, 9, 12), datetime(2015, 9, 13)]
values = [2, 4, 6, 8]

points = plt.plot(dates, values, marker="o", markerfacecolor="none")

mpld3.plugins.connect(fig, MousePositionDatePlugin())

mpld3.save_html(fig, "./mpld3_mousepositiondateplugin.html")
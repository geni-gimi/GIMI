

require 'omf-web/theme/abstract_page'
require 'labwiki/theme/column_renderer'

module OMF::Web::Theme
  class Page < OMF::Web::Theme::AbstractPage
    
    depends_on :css, "/resource/vendor/bootstrap/css/bootstrap.css"    
    depends_on :css, '/resource/theme/bright/css/reset-fonts-grids.css'
    depends_on :css, "/resource/theme/bright/css/bright.css"
    depends_on :css, "/resource/theme/labwiki/css/kaiten.css"
    depends_on :css, "/resource/theme/labwiki/css/labwiki.css"    
    
    # depends_on :js, '/resource/vendor/jquery/jquery.periodicalupdater.js'
    # depends_on :js, "/resource/vendor/jquery-ui/js/jquery-ui.min.js"
    #depends_on :js, "/resource/vendor/jquery-ui/js/jquery.ui.autocomplete.js"        

    depends_on :js, "/resource/theme/labwiki/js/column_controller.js"        
    depends_on :js, "/resource/theme/labwiki/js/content_selector_widget.js"            
    #depends_on :js, "/resource/theme/labwiki/js/execute_col_controller.js"            
    depends_on :js, "/resource/theme/labwiki/js/labwiki.js"        
   

       
    def initialize(widget, opts)
      super
      @title = "LabWiki"
      index = -1
      @col_renderers = [:plan, :prepare, :execute].map do |name|
        index += 1
        ColumnRenderer.new(name.to_s.capitalize, @widget.column_widget(name), name, index)
      end
    end
 
    def content
      javascript %{
        if (typeof(LW) == "undefined") LW = {};
        LW.session_id = OML.session_id = '#{Thread.current["sessionID"]}';
        
        L.provide('jquery', ['/resource/vendor/jquery/jquery.js']);
        L.provide('jquery.periodicalupdater', ['/resource/vendor/jquery/jquery.periodicalupdater.js']);   
        L.provide('jquery.ui', ['/resource/vendor/jquery-ui/js/jquery-ui.min.js']);
        X = null;
        /*
        $(document).ready(function() {
          X = $;
        });
        */
      }    
      div :id => "container", :style => "position: relative; height: 100%;" do
        div :id => "k-window" do
          div :id => "k-topbar" do
            span 'LabWiki', :class => 'brand'
            ul :class => 'secondary-nav' do
              li do
                a :href => '#', :class => 'user' do
                  i :class => "icon-user icon-white"
                  text 'Max'
                end
              end
              li do
                a :href => '/logout', :class => 'logout' do
                  i :class => "icon-off icon-white"
                  text 'Log out'
                end 
              end
            end
          end
          div :id => "k-slider", :style => "height: 500px;" do
            @col_renderers.each do |renderer|
              rawtext renderer.to_html
            end
          end
        end
      end
    end
    
  end # class Page
end # OMF::Web::Theme

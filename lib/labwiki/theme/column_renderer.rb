

require 'labwiki/theme/col_content_renderer'

module OMF::Web::Theme
  class ColumnRenderer < Erector::Widget
    
 
    def initialize(title, widget, col_name, position)
      @title = title
      @widget = widget
      @col_name = col_name
      @position = position
      @content_renderer = ColumnContentRenderer.new(widget, col_name)
    end
        
    def content
      title = @title
      #widget = @widget
      pos = @position
      width = 400
      style = "overflow-y: hidden; left: #{width * pos}px; width: #{width}px; display: block; " 
      div :class => "k-panel k-focus", :id => "kp#{pos}", :style => style do
        render_panel_titlebar(title)
        # div :class => "panel-options", :style => "display: none; " do
          # div :class => "block-nav" do
          # end
        # end
        render_panel_search
        rawtext @content_renderer.to_html()
        #render_widget(widget)
        div :class => "mask", :style => "display: none; " do
          div :class => "loader"
        end
      end
    end
    
    def render_panel_titlebar(title)
      div :class => "titlebar" do
        table do
          tbody do
            tr do
              td :class => "left" do
                #button :class => "tool reload", :title => "Reload"
              end
              td :class => "center" do
                div :class => "title" do
                  text title
                end
              end
              td :class => "right" do
                button :class => "tool maximize", :title => "Resize", :style => ""
                #button :class => "tool newtab", :title => "Open this panel in a new tab" 
              end
            end
          end
        end
      end
      
    end
    
    def render_panel_search
      div :class => "block-nav content-selection" do
        table do
          tr do
            unless @col_name == :plan
              td :class => 'action-buttons', :style => 'width: 32px' do
                button :class => "new-button", :onclick => "LW.#{@col_name}_controller.on_new_button();return false;"
                 #, :style => 'width:32px'
              end
            end
            td do
              form :class => "quicksearch k-active", :onsubmit => "return false;" do
                div :class => "container rounded-corners" do
                  button :class => "head_add" "FOO" # "add_content"
                  button :class => "head search"
                  input :id => "lw#{object_id}_si", :class => "input", :type => "text", :value => "" do
                    button :class => "tail reset", :onclick => "$(this).prev('input:text').val('');return false;"
                  end
                  button :class => "tail reset", :onclick => "$(this).prev('input:text').val('');return false;"
                end
              end
            end
          end
        end        
        div :id => "lw#{object_id}_sl", :class => "content-list" do
        end
        div :id => "lw#{object_id}_hi", :class => "content-list" do
          ul :class => 'content-list-history ui-menu', :style => 'display: none;' do
            ['ONE', 'TWO'].each do |item|
              li :class => 'ui-menu-item' do
                a :class => 'ui-corner-index', 'lw:url' => "http://foo/#{item}" do
                  text item
                end
              end
            end
          end
        end
      end 
      opts = {:sid => Thread.current["sessionID"], :col => @col_name}
      javascript %{
        LW.register_content_search('lw#{object_id}', #{opts.to_json});
      }
                 
    end
    
    # def render_widget(widget)
      # div :id => "col_content_#{@col_name}" do      
        # div :class => "block block-nav widget-title-block" do
          # div :class => "drop-target" do
            # div :class => "summary" do
              # div :class => 'widget-title-icon' do
                # img :src => "/resource/vendor/mono_icons/linedpaper32.png"
              # end
              # div :class => "label" do
                # text "Kaiten's documentation"
              # end
              # div :class => "info" do
              # end
            # end
          # end
        # end
        # div :class => "panel-body", :style => "height: 376px; " do
          # div :class => "block block-content widget_container" do
            # if widget
              # div :class => "widget_body widget_body_#{widget.widget_type}" do
                # rawtext widget.content().to_html 
              # end
            # else
              # 10.times do
                # p %{Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin
                    # sollicitudin nibh eu ligula lobortis ornare. Sed nibh nibh,
                    # ullamcorper at vehicula ac, molestie ac nunc. Duis sodales, nisi vel
                    # pellentesque imperdiet, nisi massa accumsan lorem, gravida scelerisque
                    # velit est vitae eros. Suspendisse eu lacinia elit.}
              # end
            # end 
#    
          # end
        # end
      # end
   # end
  end # class 
end # OMF::Web::Theme

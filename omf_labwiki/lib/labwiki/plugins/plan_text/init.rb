
module LabWiki::Plugin
  module PlanText; end
end

require 'labwiki/plugins/plan_text/plan_text_widget'
require 'labwiki/plugins/plan_text/text_renderer'

LabWiki::PluginManager.register :plan_text, {
  :widgets => [
    {
      :context => :plan,
      :priority => lambda do |opts|
        (opts[:mime_type].start_with? 'text') ? 500 : nil
      end,
      :widget_class => LabWiki::Plugin::PlanText::PlanTextWidget
    }
  ],
  :renderers => {
    :text_renderer => OMF::Web::Theme::TextRenderer
  },
  :resources => File.dirname(__FILE__) + '/resource' # should find a more portable solution
} 


# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name          = "minima"
  spec.version       = "2.5.0"
  spec.summary       = "Python and Cpp samples"
  spec.authors       = ["Chaitanya Khire"]
  spec.email         = ["devchait@github.com"]
  
  spec.add_runtime_dependency "jekyll", ">= 3.5", "< 5.0"
  spec.add_runtime_dependency "jekyll-feed", "~> 0.9"
  spec.add_runtime_dependency "jekyll-seo-tag", "~> 2.1"

  spec.add_development_dependency "bundler"
end

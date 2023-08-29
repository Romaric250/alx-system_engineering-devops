#!/usr/bin/env ruby
# A regular expression that matches 10 nums
puts ARGV[0].scan(/^[0-9]{10}$/).join

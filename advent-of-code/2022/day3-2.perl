#!/usr/bin/perl
use v5.35;

open(my $in, "<", "input/3.data") or die "Failed to find input file";

my @lines = <$in>;
my $n = scalar @lines;
my $total = 0;

for (my $i = 0; $i < $n; $i += 3) {
    my ($fst, $snd, $trd) = @lines[$i..$i + 2];

    my $common1 = "";
    my $common2 = "";

    foreach my $char (split //, $fst) {
        unless (index($snd, $char) == -1) {
            $common1 .= $char;
        }
    }

    foreach my $char (split //, $trd) {
        unless (index($common1, $char) == -1) {
            $common2 .= $char;
        }
    }

    my $common = substr $common2, 0, 1;
    if ($common =~ /\p{Uppercase}/) {
        $total += ord($common) - ord('A') + 27;
    } else {
        $total += ord($common) - ord('a') + 1;
    }
}

print "$total\n";

close $in or warn "Failed to close input file";

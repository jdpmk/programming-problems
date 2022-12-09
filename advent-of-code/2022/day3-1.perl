#!/usr/bin/perl
use v5.35;

open(my $in, "<", "input/3.data") or die "Failed to find input file";

my @lines = <$in>;
my $total = 0;

foreach my $line (@lines) {
    $line =~ s/\n//g;
    my $n = length $line;

    my $fst = substr $line, 0, $n / 2;
    my $snd = substr $line, $n / 2, $n;

    my $common = '';
    foreach my $char (split //, $fst) {
        unless (index($snd, $char) == -1) {
            $common = $char;
            last;
        }
    }

    if ($common =~ /\p{Uppercase}/) {
        $total += ord($common) - ord('A') + 27;
    } else {
        $total += ord($common) - ord('a') + 1;
    }
}

print "$total\n";

close $in or warn "Failed to close input file";
